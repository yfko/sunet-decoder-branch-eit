function gen_snr_full(snr, srcFile, outRoot)
%GEN_SNR_FULL  Re-noise ALL splits of data/v2 at one SNR level, for retraining.
%
%   gen_snr_full(20)                                % -> data/v2_full_snr20/dataset.mat
%
% PREREGISTRATION_HEART.md section 9.2 (addendum) registers a retrained contrast
% at 20 dB: arms D and B_wide trained from scratch on a dataset whose TRAINING,
% validation and test splits are all at 20 dB. gen_snr_sweep.m deliberately
% re-noises only the test split (so that the 40 dB training-split normalisation
% affine is preserved for evaluation-only sweeps); this script re-noises every
% sample, because a network retrained at 20 dB must compute its own affine from
% a 20 dB training split.
%
% Everything else is the registered procedure: tools/gen_dataset.m (hashed in
% the preregistration) is not touched; geometries come from D.geom, organ fields
% from RandStream('threefry', het_seed0 + i), measurement noise from
% noise_seed0 + i via p2_add_noise, so sample i is rebuilt exactly and the only
% change from the source is the noise amplitude. Targets (recon_lung/recon_heart,
% true_*) are carried over unchanged: they are noise-free by definition.
%
% The 40 dB self-check of gen_snr_sweep.m is repeated here on the test split
% when snr == D.snr_db, so that an inexact mesh replay is visible.

if nargin < 1 || isempty(snr),     snr = 20; end
if nargin < 2 || isempty(srcFile), srcFile = 'data/v2/dataset.mat'; end
if nargin < 3 || isempty(outRoot), outRoot = 'data'; end

here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));
if ~isfile(srcFile) && ~startsWith(srcFile, filesep), srcFile = fullfile(here, srcFile); end
if ~startsWith(outRoot, filesep) && ~isfolder(outRoot), outRoot = fullfile(here, outRoot); end
if ~isfolder(outRoot), mkdir(outRoot); end

fprintf('loading %s ...\n', srcFile);
t = tic;
S = load(srcFile);  D = S.D;  P = D.P;
fprintf('  %d samples, loaded in %.1f s; source SNR %g dB\n', D.N, toc(t), D.snr_db);

E = p2_build_env(P, fullfile(here,'results','p2_env.mat'));   % GREIT, cached

t = tic;
fmdl = ng_mk_cyl_models([2,2,D.fwd_maxsz],[P.n_elecs,1],[0.1]);
fmdl.stimulation = E.stim;
fprintf('forward mesh: %d elems (source had %d), %.1f s\n', size(fmdl.elems,1), D.n_elems, toc(t));
if size(fmdl.elems,1) ~= D.n_elems
    warning('forward mesh element count differs from the source (%d vs %d); see self-check.', ...
            size(fmdl.elems,1), D.n_elems);
end

img0 = mk_image(fmdl,1);
vh   = fwd_solve(img0);
ctr  = interp_mesh(fmdl);
zn   = ctr(:,3) - 1;
ell  = @(c,r) sum(((ctr(:,1:2) - c)/r).^2, 2) + (zn/(r*D.zscale)).^2 < 1;

recon_mixed = S.recon_mixed;
fprintf('rebuilding all %d geometries at %g dB ...\n', D.N, snr);
t0 = tic;
for i = 1:D.N
    g = D.geom(i);
    iL = find(ell(g.lung_ctr, g.r_lung) | ell([-g.lung_ctr(1) g.lung_ctr(2)], g.r_lung));
    iH = find(ell(g.heart_ctr, g.r_heart));
    iL = setdiff(iL, iH);
    if D.het_amp > 0
        rsH = RandStream('threefry','Seed', D.het_seed0 + i);
        sL = P.sig_lung  * (1 + D.het_amp * smooth_field(ctr(iL,:), D.het_modes, D.het_len, rsH));
        sH = P.sig_heart * (1 + D.het_amp * smooth_field(ctr(iH,:), D.het_modes, D.het_len, rsH));
        sL = max(sL, 0.05);  sH = max(sH, 0.05);
    else
        sL = P.sig_lung;  sH = P.sig_heart;
    end
    im = img0; im.elem_data(iL) = sL; im.elem_data(iH) = sH;
    vi  = fwd_solve(im);
    vim = p2_add_noise(vi, vh, snr, D.noise_seed0 + i);
    recon_mixed(:,:,i) = slice64(inv_solve(E.imdl, vh, vim), D.imgsz);
    if mod(i,100) == 0
        e = toc(t0);
        fprintf('  %4d/%d  %.2f s/sample  eta %.1f min\n', i, D.N, e/i, (e/i)*(D.N-i)/60);
    end
end
fprintf('  done in %.1f min\n', toc(t0)/60);

% self-check on the test split (meaningful only when snr == source level)
idxT = D.idx_test(:).';
a = S.recon_mixed(:,:,idxT);  b = recon_mixed(:,:,idxT);
fin = isfinite(a) & isfinite(b);
dmax = max(abs(a(fin) - b(fin)));  drel = dmax / max(abs(a(fin)));
if snr == D.snr_db
    fprintf('  SELF-CHECK vs source at %g dB: max abs diff %.3e (rel %.3e)\n', snr, dmax, drel);
else
    fprintf('  changed vs %g dB source on the test split: max abs diff %.3e (rel %.3e)\n', D.snr_db, dmax, drel);
end

outDir = fullfile(outRoot, sprintf('v2_full_snr%g', snr));
if ~isfolder(outDir), mkdir(outDir); end
Dout = D;
Dout.snr_db        = snr;
Dout.sweep_source  = srcFile;
Dout.sweep_note    = sprintf(['ALL splits re-noised at %g dB by gen_snr_full.m for the ' ...
                              'retrained contrast of PREREGISTRATION_HEART.md section 9.2; ' ...
                              'targets carried over unchanged'], snr);
Dout.sweep_created = datestr(now,'yyyy-mm-dd HH:MM:SS'); %#ok<TNOW1,DATST>
Dout.sweep_selfcheck_maxabs = dmax;
recon_lung = S.recon_lung;  recon_heart = S.recon_heart;
true_lung  = S.true_lung;   true_heart  = S.true_heart;
D = Dout; %#ok<NASGU>
save(fullfile(outDir,'dataset.mat'), 'recon_mixed','recon_lung','recon_heart', ...
     'true_lung','true_heart','D','-v7.3');

fid = fopen(fullfile(outDir,'PROVENANCE.txt'),'w');
fprintf(fid,'created       %s\n', Dout.sweep_created);
fprintf(fid,'source        %s (%g dB)\n', srcFile, S.D.snr_db);
fprintf(fid,'this file     %g dB on ALL splits (train %d / val %d / test %d)\n', snr, ...
        numel(D.idx_train), numel(D.idx_val), numel(idxT));
fprintf(fid,'purpose       retrained contrast, PREREGISTRATION_HEART.md section 9.2\n');
fprintf(fid,'targets       recon_lung/heart, true_* carried over unchanged\n');
fprintf(fid,'self-check    test-split max abs diff vs source %.3e (rel %.3e)\n', dmax, drel);
fclose(fid);
fprintf('wrote %s\n', fullfile(outDir,'dataset.mat'));
end

% ---- local helpers copied from tools/gen_snr_sweep.m (code identical to the frozen tools/gen_dataset.m; comments stripped there) ----
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
