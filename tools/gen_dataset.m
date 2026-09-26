function gen_dataset(N, outDir, opts)
%GEN_DATASET  Paired lung/heart EIT dataset for the divided-branch study.
%
%   gen_dataset(50,   'data/pilot')    % pilot first: confirm cost and sanity
%   gen_dataset(3600, 'data/v1')       % full run
%
% For every sampled geometry this writes three GREIT reconstructions on one
% common 64x64 raster -- mixed (lung+heart), lung only, heart only -- plus the
% analytic ground-truth conductivity field on the same raster. Everything is
% float64: no resizing, no per-frame rescaling, no JPEG. Those three steps in
% the previous pipeline are what made the reported MAE uninterpretable
% (ARS_Review_2026-08-27/08 section 2).
%
% ---------------------------------------------------------------------------
% WHY PAINTING RATHER THAN CSG MESHING
%
% p2_fwd builds a Netgen CSG mesh that conforms to the inclusions, so the mesh
% depends on r_lung and r_heart and must be rebuilt for every sample. Measured
% on this machine (Netgen 6.1 x86_64 under Rosetta 2), one such build exceeded
% 31 minutes -- 3600 of them is not a runnable plan.
%
% The inclusions are therefore PAINTED onto a plain cylinder mesh that contains
% no inclusions and so does not depend on the geometry at all: it is built once
% and reused. Per sample the cost is a vectorised element-centroid test plus
% three forward solves.
%
% This is not an invention here. It is the `cyl_paint` mode of
% ../EIT_noise_geometry/src/p2_build_geom.m, and that project measured what
% painting costs: at the cylinder reference geometry, painted and CSG
% inclusions of matched volume gave identical component selections and shape
% deformation agreeing within 0.015 (RESULTS_AXIS2.md, "Painting against
% meshing"). Cite that when the manuscript justifies the choice.
%
% ---------------------------------------------------------------------------
% HETEROGENEOUS ORGAN CONDUCTIVITY (opts.het_amp)
%
% The first study gave each organ a single constant conductivity. That left
% only six free parameters per sample (two radii, two centres), and the SNR
% pilot showed the consequence: a network trained on 2880 such samples learns
% the six-parameter manifold and emits a clean template whatever the input.
% Measured on that pilot, a model trained at 20 dB suppressed a 3.7x change in
% input noise down to a 4% change in its own output, and heart DSC stayed at
% 1.0000 from 60 dB all the way to 20 dB. The task, not the metric and not the
% noise level, was the reason nothing could discriminate.
%
% Each organ now carries a smooth random field instead:
%
%   sigma(x) = sigma_0 * (1 + a * f(x)),   f = sum of `het_modes` random
%                                          sinusoids, correlation length
%                                          `het_len`, normalised to unit
%                                          variance
%
% That raises the per-sample degrees of freedom from 6 to roughly 6 + 2 organs
% x het_modes x 5 (direction, frequency, phase) ~= 86, which is no longer
% memorisable from 2880 samples. It is also the more realistic phantom: lung
% tissue is inhomogeneous, and both the Scientific Reports referees and the
% ARS domain review (C W2) raised its absence.
%
% The same field is used for the mixed frame and for that organ's pure frame,
% so the targets stay consistent with the input.
%
% ---------------------------------------------------------------------------
% INVERSE-CRIME GUARD
%
% Painting removes the mesh difference that CSG gave for free: the plain
% forward mesh would otherwise be the same mesh the GREIT model is built on.
% So the forward mesh is built at a FINER maxsz (opts.fwd_maxsz, default 0.10)
% than the GREIT model's (P.maxsz = 0.2). Forward and inverse therefore live on
% different discretisations, which is the point.
%
% MEASUREMENT NOISE (opts.snr_db, dB)
%
% Applied to the mixed frame only -- the network's INPUT -- before
% reconstruction, because that is where instrument noise physically enters.
% The lung-only and heart-only targets stay clean: they are the definition of
% ground truth, not a measurement of it.
%
% The homogeneous reference vh also stays clean, following
% ../EIT_noise_geometry/src/p2_config.m (P.noisy_ref = false): in difference
% EIT the reference is a time-averaged baseline, so it carries far less noise
% than a single frame. A both-frames-noisy arm is a separate secondary study
% there, and would be here too.
%
% SNR follows the EIDORS convention of add_noise(SNR, v1, v2): ratio of norms
% of the difference frame to the noise, quoted in dB.
%
% ---------------------------------------------------------------------------
% REQUIREMENTS
%   MATLAB with the EIDORS v3.8 startup used by ../EIT_noise_geometry.
%   ../EIT_noise_geometry/src on the path (p2_config, p2_build_env).
%   A local copy of the GREIT cache in results/p2_env.mat, so that a parameter
%   change can never overwrite the neighbouring project's cache.

if nargin < 1 || isempty(N),      N = 50;                end
if nargin < 2 || isempty(outDir), outDir = 'data/pilot';  end
if nargin < 3, opts = struct(); end

here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));

%% ---- fixed choices, recorded with the output --------------------------
D = struct();
D.N           = N;
D.r_lung_rng  = getdef(opts,'r_lung_rng',  [0.30 0.60]);
D.r_heart_rng = getdef(opts,'r_heart_rng', [0.15 0.30]);  % 0.15 floor: see 10 s5
D.ctr_jitter  = getdef(opts,'ctr_jitter',  0.05);
D.fwd_maxsz   = getdef(opts,'fwd_maxsz',   0.10);   % finer than GREIT's 0.2
D.zscale      = getdef(opts,'zscale',      1.0);    % 1 = spheres, as CSG
D.seed        = getdef(opts,'seed',        20260828);
D.snr_db      = getdef(opts,'snr_db',      []);     % [] = noise-free
D.noise_seed0 = getdef(opts,'noise_seed0', 20260829);
% Heterogeneous conductivity inside each organ. het_amp = 0 restores the
% constant-sigma phantom of the first study.
D.het_amp     = getdef(opts,'het_amp',     0.25);   % relative SD within organ
D.het_modes   = getdef(opts,'het_modes',   8);      % random sinusoid count
D.het_len     = getdef(opts,'het_len',     0.60);   % correlation length
D.het_seed0   = getdef(opts,'het_seed0',   20260830);
D.split       = getdef(opts,'split',       [0.80 0.10 0.10]);
D.imgsz       = 64;
D.created     = datestr(now,'yyyy-mm-dd HH:MM:SS'); %#ok<TNOW1,DATST>

P = p2_config();
E = p2_build_env(P, fullfile(here,'results','p2_env.mat'));   % GREIT, cached
stim = E.stim;

rng(D.seed,'twister');
if ~isfolder(outDir), mkdir(outDir); end

%% ---- the one mesh, built once -----------------------------------------
t = tic;
fmdl = ng_mk_cyl_models([2,2,D.fwd_maxsz],[P.n_elecs,1],[0.1]);
fmdl.stimulation = stim;
fprintf('forward mesh: maxsz %.2f, %d elems, built in %.1f s\n', ...
        D.fwd_maxsz, size(fmdl.elems,1), toc(t));
D.n_elems = size(fmdl.elems,1);

img0 = mk_image(fmdl,1);
vh   = fwd_solve(img0);          % homogeneous: geometry-independent, solve once
ctr  = interp_mesh(fmdl);
zn   = ctr(:,3) - 1;             % electrode plane is z = 1
ell  = @(c,r) sum(((ctr(:,1:2) - c)/r).^2, 2) + (zn/(r*D.zscale)).^2 < 1;

%% ---- ground-truth rasteriser ------------------------------------------
% The pilot falsified the assumption that calc_slices spans [-1,1] with y up:
% this cylinder has radius 2, so the raster spans [-2,2], and the image y axis
% runs downward. Rather than hard-code a corrected grid -- still a guess -- the
% ground truth is pushed through the SAME mapping as the reconstructions: an
% image is built on the GREIT rec_model and passed to the same calc_slices.
% Any grid convention then cancels exactly.
recm = E.imdl.rec_model;
ctrT = interp_mesh(recm);
ctrR = (ctrT(1:2:end,:) + ctrT(2:2:end,:))/2;   % 2 triangles per pixel
nRec = size(ctrT,1);

%% ---- allocate ---------------------------------------------------------
recon_mixed = nan(D.imgsz, D.imgsz, N);
recon_lung  = nan(D.imgsz, D.imgsz, N);
recon_heart = nan(D.imgsz, D.imgsz, N);
true_lung   = nan(D.imgsz, D.imgsz, N);
true_heart  = nan(D.imgsz, D.imgsz, N);
ok          = false(1, N);
G = struct('r_lung',{},'r_heart',{},'lung_ctr',{},'heart_ctr',{}, ...
           'frac_lung',{},'frac_heart',{},'overlap',{}, ...
           'sig_lung_cv',{},'sig_heart_cv',{});

t0 = tic;
for i = 1:N
    g = struct();
    g.r_lung  = urand(D.r_lung_rng);
    g.r_heart = urand(D.r_heart_rng);      % INDEPENDENT of r_lung -- the point
    j = D.ctr_jitter;
    g.lung_ctr  = P.lung_ctr  + j*(2*rand(1,2)-1);
    g.heart_ctr = P.heart_ctr + j*(2*rand(1,2)-1);

    try
        iL = find(ell(g.lung_ctr, g.r_lung) | ...
                  ell([-g.lung_ctr(1) g.lung_ctr(2)], g.r_lung));
        iH = find(ell(g.heart_ctr, g.r_heart));
        % The heart wins any overlap, matching p2_build_geom: anatomically it
        % occupies the mediastinum, and numerically it keeps the heart volume
        % constant as it moves.
        g.overlap = numel(intersect(iL, iH));
        iL = setdiff(iL, iH);
        g.frac_lung  = numel(iL)/D.n_elems;
        g.frac_heart = numel(iH)/D.n_elems;
        if isempty(iL) || isempty(iH)
            error('gen:empty','empty inclusion (r_lung %.3f r_heart %.3f)', ...
                  g.r_lung, g.r_heart);
        end

        % one field per organ per sample, deterministic in the sample index
        if D.het_amp > 0
            rsH = RandStream('threefry','Seed', D.het_seed0 + i);
            sL = P.sig_lung  * (1 + D.het_amp * ...
                 smooth_field(ctr(iL,:), D.het_modes, D.het_len, rsH));
            sH = P.sig_heart * (1 + D.het_amp * ...
                 smooth_field(ctr(iH,:), D.het_modes, D.het_len, rsH));
            sL = max(sL, 0.05);  sH = max(sH, 0.05);   % keep conductivity > 0
            g.sig_lung_cv  = std(sL)/mean(sL);
            g.sig_heart_cv = std(sH)/mean(sH);
        else
            sL = P.sig_lung;  sH = P.sig_heart;
            g.sig_lung_cv = 0;  g.sig_heart_cv = 0;
        end

        im = img0; im.elem_data(iL) = sL;
                   im.elem_data(iH) = sH;   vi_m = fwd_solve(im);
        im = img0; im.elem_data(iL) = sL;   vi_l = fwd_solve(im);
        im = img0; im.elem_data(iH) = sH;   vi_h = fwd_solve(im);

        if ~isempty(D.snr_db)
            % one deterministic noise seed per sample, so any frame is
            % reproducible on its own
            vi_m = p2_add_noise(vi_m, vh, D.snr_db, D.noise_seed0 + i);
        end
        recon_mixed(:,:,i) = slice64(inv_solve(E.imdl, vh, vi_m), D.imgsz);
        recon_lung (:,:,i) = slice64(inv_solve(E.imdl, vh, vi_l), D.imgsz);
        recon_heart(:,:,i) = slice64(inv_solve(E.imdl, vh, vi_h), D.imgsz);

        % Analytic ground truth, rasterised through the same mapping. The
        % inclusions are centred at z = 1, the electrode plane, so each slice
        % is a disc.
        dl = sum((ctrR(:,1:2) - g.lung_ctr).^2, 2) < g.r_lung^2 | ...
             sum((ctrR(:,1:2) - [-g.lung_ctr(1) g.lung_ctr(2)]).^2, 2) < g.r_lung^2;
        dh = sum((ctrR(:,1:2) - g.heart_ctr).^2, 2) < g.r_heart^2;
        dl = dl & ~dh;                       % heart wins the overlap, as above
        vl = ones(size(ctrR,1),1); vl(dl) = P.sig_lung;
        vhh = ones(size(ctrR,1),1); vhh(dh) = P.sig_heart;
        true_lung (:,:,i) = raster(vl,  recm, nRec, D.imgsz);
        true_heart(:,:,i) = raster(vhh, recm, nRec, D.imgsz);

        ok(i) = true;
    catch ME
        warning('sample %d failed (%s); skipped', i, ME.message);
    end
    G(i) = g;

    if mod(i,25) == 0
        el = toc(t0);
        fprintf('%5d/%d  %.2f s/sample  eta %.1f min\n', ...
                i, N, el/i, (el/i)*(N-i)/60);
    end
end
fprintf('generated %d/%d samples in %.1f min\n', nnz(ok), N, toc(t0)/60);

%% ---- split BY GEOMETRY, not by frame ----------------------------------
idx = find(ok);
idx = idx(randperm(numel(idx)));
n   = numel(idx);
nTr = floor(D.split(1)*n);
nVa = floor(D.split(2)*n);
D.idx_train = sort(idx(1:nTr));
D.idx_val   = sort(idx(nTr+1:nTr+nVa));
D.idx_test  = sort(idx(nTr+nVa+1:end));

%% ---- save -------------------------------------------------------------
D.geom = G;  D.ok = ok;  D.P = P;
outFile = fullfile(outDir,'dataset.mat');
save(outFile,'recon_mixed','recon_lung','recon_heart', ...
             'true_lung','true_heart','D','-v7.3');
fprintf('wrote %s\n', outFile);

fid = fopen(fullfile(outDir,'PROVENANCE.txt'),'w');
fprintf(fid,'created       %s\n', D.created);
fprintf(fid,'N requested   %d\n', D.N);
fprintf(fid,'N generated   %d\n', nnz(ok));
fprintf(fid,'seed          %d\n', D.seed);
fprintf(fid,'r_lung        [%.3f %.3f]\n', D.r_lung_rng);
fprintf(fid,'r_heart       [%.3f %.3f]  (drawn independently of r_lung)\n', D.r_heart_rng);
fprintf(fid,'ctr jitter    %.3f\n', D.ctr_jitter);
fprintf(fid,'inclusions    painted (cyl_paint), zscale %.2f\n', D.zscale);
if D.het_amp > 0
    fprintf(fid,'organ sigma   heterogeneous: amp %.2f, %d modes, len %.2f, seed0 %d\n', ...
            D.het_amp, D.het_modes, D.het_len, D.het_seed0);
    fprintf(fid,'  realised CV  lung %.3f, heart %.3f\n', ...
            mean([G(ok).sig_lung_cv]), mean([G(ok).sig_heart_cv]));
else
    fprintf(fid,'organ sigma   constant (sig_lung %.2f, sig_heart %.2f)\n', ...
            P.sig_lung, P.sig_heart);
end
if isempty(D.snr_db)
    fprintf(fid,'noise         none (noise-free)\n');
else
    fprintf(fid,'noise         %.1f dB on mixed input only; targets and vh clean\n', D.snr_db);
    fprintf(fid,'noise seed0   %d (per-sample seed = seed0 + i)\n', D.noise_seed0);
end
fprintf(fid,'forward mesh  maxsz %.3f, %d elems\n', D.fwd_maxsz, D.n_elems);
fprintf(fid,'GREIT model   maxsz %.3f, imgsz [%d %d], noise_figure %.2f\n', ...
        P.maxsz, P.greit.imgsz(1), P.greit.imgsz(2), P.greit.noise_figure);
fprintf(fid,'lung vol frac %.4f +/- %.4f\n', ...
        mean([G(ok).frac_lung]), std([G(ok).frac_lung]));
fprintf(fid,'heart vol frac %.4f +/- %.4f\n', ...
        mean([G(ok).frac_heart]), std([G(ok).frac_heart]));
fprintf(fid,'split         %d / %d / %d  (by geometry)\n', ...
        numel(D.idx_train), numel(D.idx_val), numel(D.idx_test));
fprintf(fid,'phantom       n_elecs %d  sig_lung %.2f  sig_heart %.2f\n', ...
        P.n_elecs, P.sig_lung, P.sig_heart);
fclose(fid);

%% ---- alignment check, printed so a misalignment cannot pass silently ---
k = find(ok, 1);
if ~isempty(k)
    fprintf('alignment check on sample %d:\n', k);
    fprintf('  recon lung  QA centroid (%.3f, %.3f)\n', qa_centroid(recon_lung(:,:,k)));
    fprintf('  true  lung  QA centroid (%.3f, %.3f)  <- must agree\n', qa_centroid(-(true_lung(:,:,k)-1)));
    fprintf('  recon heart QA centroid (%.3f, %.3f)\n', qa_centroid(recon_heart(:,:,k)));
    fprintf('  true  heart QA centroid (%.3f, %.3f)  <- must agree\n', qa_centroid(true_heart(:,:,k)-1));
end
end

% -------------------------------------------------------------------------
function v = smooth_field(pts, n_modes, len_scale, rs)
%SMOOTH_FIELD  Zero-mean, ~unit-variance smooth random field on a point set.
%
% A sum of random plane-wave sinusoids. Cheap, smooth by construction, and its
% spatial scale is controlled directly, which matters here: the field must vary
% on a scale comparable to the organ, not pixel to pixel, or it is just noise
% and the reconstruction averages it away.
v = zeros(size(pts,1),1);
for k = 1:n_modes
    dir  = randn(rs,1,3);  dir = dir/norm(dir);
    lam  = len_scale * (0.5 + rand(rs));      % vary the scale across modes
    ph   = 2*pi*rand(rs);
    v    = v + sin(pts*dir'*(2*pi/lam) + ph);
end
v = v / sqrt(n_modes);
end

function A = raster(vals_per_pixel, recm, nRec, imgsz)
% Push an analytic field through the SAME mapping the reconstructions use, so
% no assumption about the raster's extent or y direction is needed: whatever
% calc_slices does to one, it does to the other.
gtimg = mk_image(recm, 1);
gtimg.elem_data = reshape(repmat(vals_per_pixel(:).', 2, 1), nRec, 1);
gtimg.calc_colours.ref_level = 0;
A = reshape(calc_slices(gtimg), imgsz, imgsz);
end

function c = qa_centroid(A)
A(~isfinite(A)) = 0;
m = abs(A) > 0.25*max(abs(A(:)));
[r,cc] = find(m);
c = [mean(cc), mean(r)];        % column, row -- pixel coordinates
end

function v = getdef(s,f,d)
if isfield(s,f) && ~isempty(s.(f)), v = s.(f); else, v = d; end
end

function x = urand(r)
x = r(1) + (r(2)-r(1))*rand;
end

function A = slice64(img, sz)
img.calc_colours.ref_level = 0;
A = calc_slices(img);
A = reshape(A, sz, sz);
end
