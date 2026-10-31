function R = recon_compat_check()
%RECON_COMPAT_CHECK  Staged, timed pre-hash check for PREREGISTRATION_RECON.md.
%   Every step prints its elapsed time, so a stall is visible in the log.
%   1  load the cached GREIT environment (208 measurements, adjacent drive)
%   2  Sheffield back-projection matrix: accepts our 208-value frames? raster size?
%   3  GN one-step model on the registered coarse cylinder: one solve, timed
%   4  noise figure of GREIT, BP and GN at a few hyperparameters (calc_noise_figure,
%      bounded iterations), then a bounded bisection in log10(hp) to NF = 0.5
%   5  raster alignment: argmin (lung) and argmax (heart) pixels of the three
%      reconstructions of the environment's reference frame
here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));
T = tic; stamp = @(s) fprintf('[%7.1f s] %s\n', toc(T), s);

stamp('1 load environment');
S = load(fullfile(here,'results','p2_env.mat')); E = S.E;
fprintf('   measurements per frame: %d\n', numel(E.vh.meas));
imgG = inv_solve(E.imdl, E.vh, E.vi); A = slice64(imgG);
fprintf('   GREIT raster %s, NaN fraction %.3f\n', mat2str(size(A)), mean(isnan(A(:))));

stamp('2 Sheffield back-projection');
imBP = mk_common_gridmdl('backproj');
fprintf('   RM %s, meas_select %d\n', mat2str(size(imBP.solve_use_matrix.RM)), nnz(imBP.fwd_model.meas_select));
try
    imgB = inv_solve(imBP, E.vh, E.vi); B = slice64(imgB);
    fprintf('   BP raster %s, NaN fraction %.3f\n', mat2str(size(B)), mean(isnan(B(:))));
    R.bp_ok = true;
catch ME
    fprintf('   BP FAILED: %s\n', ME.message); R.bp_ok = false; B = [];
end

stamp('3 GN one-step model');
fmdlG = ng_mk_cyl_models([2,2,0.2],[16,1],[0.1]);
fmdlG.stimulation = E.stim; fmdlG = mdl_normalize(fmdlG,1);
fprintf('   GN mesh: %d elements\n', size(fmdlG.elems,1));
imGN = eidors_obj('inv_model','GN');
imGN.fwd_model = fmdlG; imGN.reconst_type = 'difference';
imGN.solve = @inv_solve_diff_GN_one_step; imGN.RtR_prior = @prior_laplace;
imGN.jacobian_bkgnd.value = 1;
% solve on GREIT's own 64x64 reconstruction grid (coarse-to-fine mapping): the
% inverse is then a few-thousand-unknown problem, and GN images land on exactly
% the GREIT raster, so no resampling or alignment step is needed
imGN.rec_model = E.imdl.rec_model;
t = tic; imGN.fwd_model.coarse2fine = mk_coarse_fine_mapping(fmdlG, E.imdl.rec_model);
fprintf('   coarse2fine %s (%.1f s); rec elements %d\n', mat2str(size(imGN.fwd_model.coarse2fine)), toc(t), size(E.imdl.rec_model.elems,1));
imGN.hyperparameter.value = 1e-2;
t = tic; imgN = inv_solve(imGN, E.vh, E.vi); fprintf('   first GN solve (Jacobian + prior) %.1f s\n', toc(t));
t = tic; imgN = inv_solve(imGN, E.vh, E.vi); fprintf('   second GN solve (cached) %.2f s\n', toc(t));
C = slice64(imgN);

stamp('4 noise figures');
ctr = interp_mesh(fmdlG);
tg = find(sum(ctr(:,1:2).^2,2) < 0.2^2 & abs(ctr(:,3)-1) < 0.2);
fprintf('   central target elements: %d\n', numel(tg));
vh0 = E.vh.meas(:); vi0 = E.vi.meas(:);   % one reference target (the environment phantom) for all three NFs
t = tic; R.nf_greit = calc_noise_figure(E.imdl, vh0, vi0); fprintf('   NF GREIT %.3f (%.1f s)\n', R.nf_greit, toc(t));
if R.bp_ok
    t = tic; R.nf_bp = calc_noise_figure(imBP, vh0, vi0); fprintf('   NF BP %.3f (%.1f s)\n', R.nf_bp, toc(t));
end
nf = @(hp) calc_noise_figure(sethp(imGN, hp), vh0, vi0);
lo = -5; hi = 1; target = R.nf_greit;   % match GREIT's realised NF on the same target   % log10 hyperparameter bracket; NF falls as hp rises
t = tic; fl = nf(10^lo); fh = nf(10^hi);
fprintf('   NF(1e%d)=%.3f  NF(1e%d)=%.3f  (%.1f s)\n', lo, fl, hi, fh, toc(t));
for k = 1:12
    mid = (lo+hi)/2; fm = nf(10^mid);
    fprintf('   bisect %2d: hp=1e%.3f NF=%.3f (%.1f s)\n', k, mid, fm, toc(t));
    if (fm - target) > 0, lo = mid; else, hi = mid; end
    if abs(fm - target) < 0.02, break; end
end
R.gn_hp = 10^mid; R.gn_nf = fm;
fprintf('   GN hyperparameter %.4g gives NF %.3f\n', R.gn_hp, R.gn_nf);

stamp('5 raster alignment on the environment reference frame');
imGN.hyperparameter = struct('value', R.gn_hp);
C = slice64(inv_solve(imGN, E.vh, E.vi));
pk = @(X, f) ind2sub_(size(X), f(X(:)));
[~, ga] = min(A(:)); [~, ca] = min(C(:));
fprintf('   lung minimum pixel: GREIT %s  GN %s\n', mat2str(idx(size(A),ga)), mat2str(idx(size(C),ca)));
if ~isempty(B)
    [~, ba] = min(B(:)); fprintf('   lung minimum pixel: BP %s (raster %s)\n', mat2str(idx(size(B),ba)), mat2str(size(B)));
end
[~, gh] = max(A(:)); [~, ch] = max(C(:));
fprintf('   heart maximum pixel: GREIT %s  GN %s\n', mat2str(idx(size(A),gh)), mat2str(idx(size(C),ch)));
stamp('done');
save(fullfile(here,'results','recon_compat_check.mat'),'R');
end

function A = slice64(img)
img.calc_colours.ref_level = 0; A = calc_slices(img);
end
function v = idx(sz, i)
[r,c] = ind2sub(sz, i); v = [r c];
end
function v = ind2sub_(sz, i) %#ok<DEFNU>
[r,c] = ind2sub(sz, i); v = [r c];
end
function m = sethp(m, hp)
m.hyperparameter = struct('value', hp);
end
