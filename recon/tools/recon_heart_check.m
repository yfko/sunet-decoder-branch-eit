function recon_heart_check()
% Heart-only and lung-only frames through GREIT, GN (on GREIT's grid) and BP:
% where is the peak, and how large is the quarter-amplitude set?
here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));
S = load(fullfile(here,'results','p2_env.mat')); E = S.E;
R = load(fullfile(here,'results','recon_compat_check.mat')); R = R.R;
fmdlG = ng_mk_cyl_models([2,2,0.2],[16,1],[0.1]); fmdlG.stimulation = E.stim; fmdlG = mdl_normalize(fmdlG,1);
imGN = eidors_obj('inv_model','GN'); imGN.fwd_model = fmdlG; imGN.reconst_type='difference';
imGN.solve=@inv_solve_diff_GN_one_step; imGN.RtR_prior=@prior_laplace; imGN.jacobian_bkgnd.value=1;
imGN.rec_model = E.imdl.rec_model; imGN.fwd_model.coarse2fine = mk_coarse_fine_mapping(fmdlG, E.imdl.rec_model);
imGN.hyperparameter.value = R.gn_hp;
imBP = mk_common_gridmdl('backproj');
vh = E.vh; fov = [];
for comp = {'heart','lung'}
    d = E.(['d_' comp{1}]);  vi = vh; vi.meas = vh.meas(:) + d(:);
    G = sl(inv_solve(E.imdl, vh, vi));
    N = sl(inv_solve(imGN, vh, vi));
    B = kron(sl(inv_solve(imBP, vh, vi)), ones(2));
    if isempty(fov), fov = isfinite(G); end
    g=G(fov); n=N(fov); c=corrcoef(g,n); fprintf('%-6s GREIT vs GN: corr %.4f, max|diff|/max|G| %.3f, max|G| %.3g max|N| %.3g\n', comp{1}, c(1,2), max(abs(g-n))/max(abs(g)), max(abs(g)), max(abs(n)));
    imgs = struct('GREIT', G, 'GN', N, 'BP', B);
    for nm = {'GREIT','GN','BP'}
        X = imgs.(nm{1}); X(~fov) = NaN;
        s = sign(sum(X(fov))); Y = s*X;                    % organ sign: heart +, lung - in these difference images
        [~, k] = max(Y(:)); [r, c] = ind2sub(size(Y), k);
        qa = abs(X) > 0.25*max(abs(X(fov))); qa = qa & fov;
        fprintf('%-6s %-5s peak at [%2d %2d]  QA fraction of FOV %.3f\n', comp{1}, nm{1}, r, c, nnz(qa)/nnz(fov));
    end
end
end
function A = sl(img)
img.calc_colours.ref_level = 0; A = calc_slices(img);
end
