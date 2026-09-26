function gen_snr_sweep(levels, srcFile, outRoot)
%GEN_SNR_SWEEP  Re-noise the TEST split of data/v2 at several SNR levels, for H3.
%
%   gen_snr_sweep                                   % 60 50 40 30 20 dB, defaults
%   gen_snr_sweep([30 20])                          % just the low end
%
% PREREGISTRATION_HEART.md section 5 registers an evaluation-only SNR sweep at
% 60/50/40/30/20 dB, and section 3 tests H3 on it: the D - B_wide advantage should
% GROW as SNR falls. Models are trained once at 40 dB and evaluated across the
% sweep, so nothing is retrained here.
%
% ---------------------------------------------------------------------------
% WHY THIS IS A NEW FILE
%
% tools/gen_dataset.m is named in the hashed preregistration of this study and
% is not touched. This script only reads its output.
%
% ---------------------------------------------------------------------------
% WHY ONLY THE TEST SPLIT, AND WHY THE OUTPUT KEEPS THE FULL SHAPE
%
% Only recon_mixed -- the network INPUT -- carries noise. recon_lung/recon_heart
% are the targets and are noise-free by definition, so they are carried over from
% the source file untouched, which also guarantees they are byte-identical to the
% ones the 40 dB evaluation scored against.
%
% The output keeps all N samples and the original D.idx_train/val/test, with only
% the test samples' recon_mixed replaced. That is deliberate:
% tools/train_arms.py:normalise() computes ONE affine from the TRAINING split of
% whatever file is loaded. Keeping the training split byte-identical makes that
% affine reproduce exactly the mu/sd recorded in runs/run_meta.json, so
% tools/evaluate.py needs no modification and no new code path -- point --data at
% one of these files and everything else is unchanged. A file containing only the
% 360 test samples would have silently renormalised every image.
%
% ---------------------------------------------------------------------------
% HOW A SAMPLE IS REPRODUCED WITHOUT REPLAYING THE GEOMETRY RNG
%
% gen_dataset.m records every sampled geometry in D.geom(i) (r_lung, r_heart,
% both centres) and both derived RNG streams are deterministic in the sample
% index: the organ conductivity field uses RandStream('threefry', het_seed0 + i)
% and the measurement noise uses noise_seed0 + i. So sample i is rebuilt exactly
% from stored parameters -- no dependence on how many rand() calls preceded it.
%
% The forward mesh is rebuilt by ng_mk_cyl_models with the same arguments. Netgen
% is *expected* to be deterministic, but that is not assumed: this script always
% regenerates the 40 dB level as well and reports its agreement with the source
% file. Read that number before trusting the others.
%
%   agreement exact (0, or ~1e-12)  -> the replay is the same mesh; the sweep can
%                                      be compared against the original 40 dB run
%   agreement poor                  -> the mesh differs; use THIS file's 40 dB
%                                      level as H3's high-SNR anchor instead, so
%                                      all five levels share one mesh and the
%                                      comparison between levels stays clean
%
% Either way H3 is answerable, because H3 compares levels to each other.

if nargin < 1 || isempty(levels),  levels = [60 50 40 30 20]; end
if nargin < 2 || isempty(srcFile), srcFile = 'data/v2/dataset.mat'; end
if nargin < 3 || isempty(outRoot), outRoot = 'data'; end

here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));
% a relative path is relative to the project root, not to whatever cwd
% MATLAB happens to be in; an absolute path is used as given even if it does
% not exist yet (it is created below).
if ~isfile(srcFile) && ~startsWith(srcFile, filesep)
    srcFile = fullfile(here, srcFile);
end
if ~startsWith(outRoot, filesep) && ~isfolder(outRoot)
    outRoot = fullfile(here, outRoot);
end
if ~isfolder(outRoot), mkdir(outRoot); end

if ~ismember(40, levels)
    warning('40 dB added to the sweep: it is the self-check against the source.');
    levels = unique([40 levels], 'stable');
end

%% ---- source -------------------------------------------------------------
fprintf('loading %s ...\n', srcFile);
t = tic;
S = load(srcFile);              % recon_mixed/lung/heart, true_*, D
D = S.D;  P = D.P;
fprintf('  %d samples, loaded in %.1f s\n', D.N, toc(t));

idxT = D.idx_test(:).';
fprintf('  test split: %d geometries (idx %d..%d)\n', numel(idxT), min(idxT), max(idxT));
fprintf('  source SNR: %g dB, noise_seed0 %d, het_seed0 %d\n', ...
        D.snr_db, D.noise_seed0, D.het_seed0);

%% ---- the same environment gen_dataset.m used ---------------------------
E = p2_build_env(P, fullfile(here,'results','p2_env.mat'));   % GREIT, cached

t = tic;
fmdl = ng_mk_cyl_models([2,2,D.fwd_maxsz],[P.n_elecs,1],[0.1]);
fmdl.stimulation = E.stim;
fprintf('forward mesh: maxsz %.2f, %d elems (source had %d), built in %.1f s\n', ...
        D.fwd_maxsz, size(fmdl.elems,1), D.n_elems, toc(t));
if size(fmdl.elems,1) ~= D.n_elems
    warning(['forward mesh has a DIFFERENT element count than the source ' ...
             '(%d vs %d). The 40 dB self-check below will quantify what that ' ...
             'costs; use this run''s own 40 dB level as the anchor.'], ...
            size(fmdl.elems,1), D.n_elems);
end

img0 = mk_image(fmdl,1);
vh   = fwd_solve(img0);
ctr  = interp_mesh(fmdl);
zn   = ctr(:,3) - 1;
ell  = @(c,r) sum(((ctr(:,1:2) - c)/r).^2, 2) + (zn/(r*D.zscale)).^2 < 1;

%% ---- rebuild each test sample's conductivity ONCE, reuse across levels --
% The organ fields do not depend on SNR, so the painting and the smooth random
% fields are done once and only the noise + inverse solve repeat per level.
fprintf('rebuilding %d test geometries ...\n', numel(idxT));
t0 = tic;
VI = cell(1, numel(idxT));            % clean mixed frames
for k = 1:numel(idxT)
    i = idxT(k);  g = D.geom(i);
    iL = find(ell(g.lung_ctr, g.r_lung) | ...
              ell([-g.lung_ctr(1) g.lung_ctr(2)], g.r_lung));
    iH = find(ell(g.heart_ctr, g.r_heart));
    iL = setdiff(iL, iH);             % heart wins the overlap, as in gen_dataset
    if D.het_amp > 0
        rsH = RandStream('threefry','Seed', D.het_seed0 + i);
        sL = P.sig_lung  * (1 + D.het_amp * ...
             smooth_field(ctr(iL,:), D.het_modes, D.het_len, rsH));
        sH = P.sig_heart * (1 + D.het_amp * ...
             smooth_field(ctr(iH,:), D.het_modes, D.het_len, rsH));
        sL = max(sL, 0.05);  sH = max(sH, 0.05);
    else
        sL = P.sig_lung;  sH = P.sig_heart;
    end
    im = img0; im.elem_data(iL) = sL; im.elem_data(iH) = sH;
    VI{k} = fwd_solve(im);
    if mod(k,50) == 0
        e = toc(t0);
        fprintf('  %4d/%d  %.2f s/sample  eta %.1f min\n', ...
                k, numel(idxT), e/k, (e/k)*(numel(idxT)-k)/60);
    end
end
fprintf('  forward solves done in %.1f min\n', toc(t0)/60);

%% ---- one output file per level -----------------------------------------
for snr = levels(:).'
    fprintf('\n=== %g dB ===\n', snr);
    outDir = fullfile(outRoot, sprintf('v2_snr%g', snr));
    if ~isfolder(outDir), mkdir(outDir); end

    recon_mixed = S.recon_mixed;      % everything else carried over untouched
    t0 = tic;
    for k = 1:numel(idxT)
        i   = idxT(k);
        vim = p2_add_noise(VI{k}, vh, snr, D.noise_seed0 + i);
        recon_mixed(:,:,i) = slice64(inv_solve(E.imdl, vh, vim), D.imgsz);
    end
    fprintf('  inverse solves: %.1f min\n', toc(t0)/60);

    % --- self-check against the source, on the test split only
    a = S.recon_mixed(:,:,idxT);  b = recon_mixed(:,:,idxT);
    fin = isfinite(a) & isfinite(b);
    dmax = max(abs(a(fin) - b(fin)));
    drel = dmax / max(abs(a(fin)));
    if snr == D.snr_db
        fprintf('  SELF-CHECK vs source at %g dB: max abs diff %.3e (rel %.3e)\n', ...
                snr, dmax, drel);
        if drel < 1e-9
            fprintf('  -> EXACT replay. The sweep is comparable to the original runs.\n');
        else
            fprintf(['  -> NOT exact. Use THIS file''s 40 dB level as H3''s\n' ...
                     '     high-SNR anchor; all five levels then share one mesh.\n']);
        end
    else
        fprintf('  changed vs 40 dB source: max abs diff %.3e (rel %.3e)\n', dmax, drel);
    end

    Dout = D;
    Dout.snr_db       = snr;
    Dout.sweep_source = srcFile;
    Dout.sweep_note   = sprintf(['test split re-noised at %g dB by ' ...
        'gen_snr_sweep.m; train/val samples and all targets carried over ' ...
        'from the source unchanged'], snr);
    Dout.sweep_created = datestr(now,'yyyy-mm-dd HH:MM:SS'); %#ok<TNOW1,DATST>
    Dout.sweep_selfcheck_maxabs = dmax;

    recon_lung = S.recon_lung;  recon_heart = S.recon_heart;
    true_lung  = S.true_lung;   true_heart  = S.true_heart;
    D = Dout; %#ok<NASGU>
    save(fullfile(outDir,'dataset.mat'), 'recon_mixed','recon_lung', ...
         'recon_heart','true_lung','true_heart','D','-v7.3');
    D = S.D;                          % restore for the next level

    fid = fopen(fullfile(outDir,'PROVENANCE.txt'),'w');
    fprintf(fid,'created       %s\n', Dout.sweep_created);
    fprintf(fid,'source        %s (%g dB)\n', srcFile, S.D.snr_db);
    fprintf(fid,'this level    %g dB on the TEST split only (%d geometries)\n', ...
            snr, numel(idxT));
    fprintf(fid,'carried over  train/val recon_mixed, and ALL targets, unchanged\n');
    fprintf(fid,'  -> the training-split normalisation affine is unchanged, so\n');
    fprintf(fid,'     tools/evaluate.py needs no modification for this file\n');
    fprintf(fid,'noise seed0   %d (per-sample seed = seed0 + i), same as source\n', ...
            D.noise_seed0);
    fprintf(fid,'organ sigma   rebuilt from D.geom + het_seed0 %d, identical to source\n', ...
            D.het_seed0);
    fprintf(fid,'forward mesh  maxsz %.3f, %d elems (source %d)\n', ...
            D.fwd_maxsz, size(fmdl.elems,1), D.n_elems);
    fprintf(fid,'self-check    max abs diff vs source on test split: %.3e (rel %.3e)\n', ...
            dmax, drel);
    fprintf(fid,'registered by PREREGISTRATION_HEART.md sections 3 (H3) and 5\n');
    fclose(fid);
    fprintf('  wrote %s\n', fullfile(outDir,'dataset.mat'));
end

fprintf('\nsweep complete: %s\n', strjoin(compose('%g dB', levels(:).'), ', '));
end

% -------------------------------------------------------------------------
% Copied verbatim from tools/gen_dataset.m, which is frozen by the hashed
% preregistration and therefore cannot export them.
function v = smooth_field(pts, n_modes, len_scale, rs)
v = zeros(size(pts,1),1);
for k = 1:n_modes
    dir  = randn(rs,1,3);  dir = dir/norm(dir);
    lam  = len_scale * (0.5 + rand(rs));
    ph   = 2*pi*rand(rs);
    v    = v + sin(pts*dir'*(2*pi/lam) + ph);
end
v = v / sqrt(n_modes);
end

function A = slice64(img, sz)
img.calc_colours.ref_level = 0;
A = calc_slices(img);
A = reshape(A, sz, sz);
end
