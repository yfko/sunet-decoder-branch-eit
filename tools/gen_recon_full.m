function gen_recon_full(snr, srcFile, outRoot)
%GEN_RECON_FULL  Rebuild data/v2 at one SNR with two further reconstructors.
%
%   gen_recon_full(20)    % -> data/v2_full_snr20_gn/, data/v2_full_snr20_bp/,
%                         %    data/v2_voltages/, data/v2_test_snr40_{gn,bp}/
%
% PREREGISTRATION_RECON.md (hash in PREREGISTRATION_RECON.sha256) registers a
% 3x3 training-by-evaluation reconstructor matrix at 20 dB. This script produces
% the two non-GREIT datasets exactly as gen_snr_full.m produces the GREIT one:
% the registered geometries (D.geom), organ fields (threefry het_seed0 + i) and
% measurement noise (noise_seed0 + i) are replayed, so sample i is bit-for-bit
% the same boundary-voltage frame in every dataset; only the reconstruction
% operator differs. Targets are each reconstructor's own single-organ
% reconstructions (as in gen_dataset.m); the analytic true_* rasters are
% carried over unchanged.
%
% Reconstructors (section 4 of the preregistration):
%   GN  inv_solve_diff_GN_one_step, prior_laplace, on the registered coarse
%       cylinder (maxsz 0.2, normalised difference like the GREIT model),
%       hyperparameter from choose_noise_figure at NF 0.5 (GREIT's setting).
%   BP  mk_common_gridmdl('backproj'), the Sheffield MKI back-projection matrix
%       (inv_solve_backproj is documented as incomplete in EIDORS 3.8).
%
% Also written, once, because they are reconstructor-independent:
%   data/v2_voltages/voltages_snr<snr>.mat  vh, vi_m_clean, vi_m_noisy, vi_l, vi_h
%   (208 x N each) for the measurement-domain line.
% And, for the registered secondary 3(a) (image-domain perturbation 40 -> 20 dB),
% the TEST split re-noised at 40 dB and reconstructed with GN and BP.

if nargin < 1 || isempty(snr),     snr = 20; end
if nargin < 2 || isempty(srcFile), srcFile = 'data/v2/dataset.mat'; end
if nargin < 3 || isempty(outRoot), outRoot = 'data'; end
here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));
if ~isfile(srcFile) && ~startsWith(srcFile, filesep), srcFile = fullfile(here, srcFile); end
if ~startsWith(outRoot, filesep) && ~isfolder(outRoot), outRoot = fullfile(here, outRoot); end

fprintf('loading %s ...\n', srcFile); t = tic;
S = load(srcFile);  D = S.D;  P = D.P;
fprintf('  %d samples, %.1f s; source SNR %g dB\n', D.N, toc(t), D.snr_db);
E = p2_build_env(P, fullfile(here,'results','p2_env.mat'));   % GREIT, cached (for the replay self-check)

%% ---- reconstructors ------------------------------------------------------
fmdlG = ng_mk_cyl_models([2,2,P.maxsz],[P.n_elecs,1],[0.1]);
fmdlG.stimulation = E.stim;
fmdlG = mdl_normalize(fmdlG,1);
imGN = eidors_obj('inv_model','GN one-step, Laplace prior, NF-matched');
imGN.fwd_model = fmdlG;  imGN.reconst_type = 'difference';
imGN.solve = @inv_solve_diff_GN_one_step;  imGN.RtR_prior = @prior_laplace;
imGN.jacobian_bkgnd.value = 1;
ctrG = interp_mesh(fmdlG);
tg = find(sum(ctrG(:,1:2).^2,2) < 0.2^2 & abs(ctrG(:,3)-1) < 0.2);   % central target for NF
imGN.hyperparameter.func = @choose_noise_figure;
imGN.hyperparameter.noise_figure = P.greit.noise_figure;               % 0.5, as GREIT
imGN.hyperparameter.tgt_elems = tg;
t = tic; HP = choose_noise_figure(imGN); tHP = toc(t);
imGN.hyperparameter = struct('value', HP);
R.gn_hyperparameter = HP;  R.gn_tgt_elems = numel(tg);
R.gn_nf_check = calc_noise_figure(imGN, E.vh, E.vi);
fprintf('GN: hyperparameter %.4g for NF %.2f (%.0f s); NF on the env target %.3f\n', HP, P.greit.noise_figure, tHP, R.gn_nf_check);

imBP = mk_common_gridmdl('backproj');
R.bp_nf_check = calc_noise_figure(imBP, E.vh, E.vi);
R.greit_nf_check = calc_noise_figure(E.imdl, E.vh, E.vi);
fprintf('BP: Sheffield matrix %s; NF on the env target %.3f (GREIT %.3f)\n', mat2str(size(imBP.solve_use_matrix.RM)), R.bp_nf_check, R.greit_nf_check);

%% ---- forward model replay (identical to gen_snr_full.m) ------------------
t = tic;
fmdl = ng_mk_cyl_models([2,2,D.fwd_maxsz],[P.n_elecs,1],[0.1]);
fmdl.stimulation = E.stim;
fprintf('forward mesh: %d elems (source had %d), %.1f s\n', size(fmdl.elems,1), D.n_elems, toc(t));
if size(fmdl.elems,1) ~= D.n_elems
    warning('forward mesh element count differs from the source (%d vs %d); see self-check.', size(fmdl.elems,1), D.n_elems);
end
img0 = mk_image(fmdl,1);
vh   = fwd_solve(img0);
ctr  = interp_mesh(fmdl);
zn   = ctr(:,3) - 1;
ell  = @(c,r) sum(((ctr(:,1:2) - c)/r).^2, 2) + (zn/(r*D.zscale)).^2 < 1;

N = D.N; sz = D.imgsz; nm = numel(vh.meas);
gn = struct('mixed', nan(sz,sz,N), 'lung', nan(sz,sz,N), 'heart', nan(sz,sz,N));
bp = gn;
V  = struct('vh', double(vh.meas(:)), 'vi_m_clean', nan(nm,N), 'vi_m_noisy', nan(nm,N), 'vi_l', nan(nm,N), 'vi_h', nan(nm,N));
selfchk = nan(1,3);   % GREIT replay of the first three test frames vs v2_full_snr20

full20 = fullfile(outRoot, 'v2_full_snr20', 'dataset.mat');
if isfile(full20)
    F = matfile(full20);
else
    F = []; warning('%s not found: GREIT replay self-check skipped', full20);
end
idxT = D.idx_test(:).';

fprintf('rebuilding %d geometries at %g dB with GN and BP ...\n', N, snr);
t0 = tic;
for i = 1:N
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
    im = img0; im.elem_data(iL) = sL; im.elem_data(iH) = sH;   vi_m = fwd_solve(im);
    im = img0; im.elem_data(iL) = sL;                           vi_l = fwd_solve(im);
    im = img0; im.elem_data(iH) = sH;                           vi_h = fwd_solve(im);
    vim = p2_add_noise(vi_m, vh, snr, D.noise_seed0 + i);

    V.vi_m_clean(:,i) = double(vi_m.meas(:));  V.vi_m_noisy(:,i) = double(vim.meas(:));
    V.vi_l(:,i) = double(vi_l.meas(:));        V.vi_h(:,i) = double(vi_h.meas(:));

    gn.mixed(:,:,i) = slice64(inv_solve(imGN, vh, vim),  sz);
    gn.lung (:,:,i) = slice64(inv_solve(imGN, vh, vi_l), sz);
    gn.heart(:,:,i) = slice64(inv_solve(imGN, vh, vi_h), sz);
    bp.mixed(:,:,i) = slice64(inv_solve(imBP, vh, vim),  sz);
    bp.lung (:,:,i) = slice64(inv_solve(imBP, vh, vi_l), sz);
    bp.heart(:,:,i) = slice64(inv_solve(imBP, vh, vi_h), sz);

    k = find(idxT(1:min(3,end)) == i, 1);
    if ~isempty(k) && ~isempty(F)
        a = F.recon_mixed(:,:,i);  b = slice64(inv_solve(E.imdl, vh, vim), sz);
        fin = isfinite(a) & isfinite(b);
        selfchk(k) = max(abs(a(fin) - b(fin))) / max(abs(a(fin)));
    end
    if mod(i,100) == 0
        e = toc(t0); fprintf('  %4d/%d  %.2f s/sample  eta %.1f min\n', i, N, e/i, (e/i)*(N-i)/60);
    end
end
fprintf('  done in %.1f min\n', toc(t0)/60);
R.greit_replay_selfcheck_rel = selfchk;
fprintf('GREIT replay self-check (rel max abs diff, 3 test frames): %s\n', mat2str(selfchk, 3));

%% ---- test split at 40 dB, mixed only, for secondary 3(a) ------------------
fprintf('test split at 40 dB (mixed only) for the perturbation secondary ...\n');
t40 = struct('gn', nan(sz,sz,numel(idxT)), 'bp', nan(sz,sz,numel(idxT)));
for k = 1:numel(idxT)
    i = idxT(k);
    vi_m = vh; vi_m.meas = V.vi_m_clean(:,i);
    vim40 = p2_add_noise(vi_m, vh, 40, D.noise_seed0 + i);
    t40.gn(:,:,k) = slice64(inv_solve(imGN, vh, vim40), sz);
    t40.bp(:,:,k) = slice64(inv_solve(imBP, vh, vim40), sz);
end

%% ---- save ------------------------------------------------------------------
true_lung = S.true_lung;  true_heart = S.true_heart; %#ok<NASGU>
for tag = {'gn','bp'}
    T = tag{1};
    if strcmp(T,'gn'), Q = gn; else, Q = bp; end
    outDir = fullfile(outRoot, sprintf('v2_full_snr%g_%s', snr, T));
    if ~isfolder(outDir), mkdir(outDir); end
    Dout = D;  Dout.snr_db = snr;  Dout.reconstructor = T;  Dout.recon_info = R;
    Dout.sweep_source = srcFile;
    Dout.sweep_note = sprintf(['ALL splits re-noised at %g dB and reconstructed with %s by gen_recon_full.m ' ...
        'for PREREGISTRATION_RECON.md; targets are this reconstructor''s single-organ reconstructions; ' ...
        'true_* carried over'], snr, upper(T));
    Dout.sweep_created = datestr(now,'yyyy-mm-dd HH:MM:SS'); %#ok<TNOW1,DATST>
    recon_mixed = Q.mixed; recon_lung = Q.lung; recon_heart = Q.heart; %#ok<NASGU>
    D_save = Dout;
    save_ds(fullfile(outDir,'dataset.mat'), recon_mixed, recon_lung, recon_heart, true_lung, true_heart, D_save);
    fid = fopen(fullfile(outDir,'PROVENANCE.txt'),'w');
    fprintf(fid,'created       %s\n', Dout.sweep_created);
    fprintf(fid,'source        %s (%g dB geometries/seeds)\n', srcFile, S.D.snr_db);
    fprintf(fid,'reconstructor %s\n', upper(T));
    if strcmp(T,'gn'), fprintf(fid,'GN            one-step, Laplace prior, NF %.2f -> hyperparameter %.6g (tgt elems %d); NF check %.3f\n', P.greit.noise_figure, R.gn_hyperparameter, R.gn_tgt_elems, R.gn_nf_check);
    else, fprintf(fid,'BP            mk_common_gridmdl(''backproj''), Sheffield MKI matrix; NF check %.3f (GREIT %.3f)\n', R.bp_nf_check, R.greit_nf_check); end
    fprintf(fid,'this file     %g dB on ALL splits (train %d / val %d / test %d)\n', snr, numel(D.idx_train), numel(D.idx_val), numel(idxT));
    fprintf(fid,'GREIT replay  rel max abs diff on 3 test frames vs v2_full_snr20: %s\n', mat2str(selfchk,3));
    fprintf(fid,'purpose       PREREGISTRATION_RECON.md 3x3 reconstructor matrix\n');
    fclose(fid);
    fprintf('wrote %s\n', outDir);
    % 40 dB test split (mixed only)
    outT = fullfile(outRoot, sprintf('v2_test_snr40_%s', T));
    if ~isfolder(outT), mkdir(outT); end
    recon_mixed_test40 = t40.(T); idx_test = idxT; %#ok<NASGU>
    save(fullfile(outT,'test40.mat'), 'recon_mixed_test40', 'idx_test', '-v7.3');
end
vdir = fullfile(outRoot, 'v2_voltages'); if ~isfolder(vdir), mkdir(vdir); end
V.note = sprintf('208 x N boundary voltages, adjacent drive, no_meas_current; noise %g dB on vi_m_noisy only (seed noise_seed0+i); geometries data/v2', snr);
V.snr_db = snr; V.idx_train = D.idx_train; V.idx_val = D.idx_val; V.idx_test = D.idx_test;
save(fullfile(vdir, sprintf('voltages_snr%g.mat', snr)), '-struct', 'V', '-v7.3');
fprintf('wrote %s\n', vdir);
end

% ---- helpers (code identical to the frozen tools/gen_dataset.m) ----------
function save_ds(f, recon_mixed, recon_lung, recon_heart, true_lung, true_heart, D) %#ok<INUSD>
save(f, 'recon_mixed','recon_lung','recon_heart','true_lung','true_heart','D','-v7.3');
end
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
