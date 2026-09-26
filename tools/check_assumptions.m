% Verify the three ASSUMPTION markers in gen_dataset.m before a full run.
% Uses a LOCAL copy of the GREIT cache so nothing in ../EIT_noise_geometry
% can be overwritten.
here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));
addpath(fullfile(here,'tools'));

P = p2_config();
fprintf('P: n_elecs=%d maxsz=%.2f r_lung=%.2f r_heart=%.2f lung_ctr=[%.2f %.2f] heart_ctr=[%.2f %.2f]\n', ...
        P.n_elecs, P.maxsz, P.r_lung, P.r_heart, P.lung_ctr, P.heart_ctr);
fprintf('GREIT imgsz=[%d %d]\n', P.greit.imgsz);

E = p2_build_env(P, fullfile(here,'results','p2_env.mat'));
fprintf('env loaded. imdl ok=%d  stim ok=%d\n', ~isempty(E.imdl), ~isempty(E.stim));

geom = struct('r_lung',0.45,'r_heart',0.20, ...
              'lung_ctr',P.lung_ctr,'heart_ctr',P.heart_ctr);
t=tic;
[~, vh, vi] = p2_fwd(P, P.maxsz, E.stim, true, true, geom);
fprintf('p2_fwd (mixed) OK in %.1f s; meas length=%d\n', toc(t), numel(vi.meas));

img = inv_solve(E.imdl, vh, vi);
img.calc_colours.ref_level = 0;
A = calc_slices(img);
fprintf('ASSUMPTION-1 calc_slices size = [%s]  class=%s\n', ...
        num2str(size(A)), class(A));
fprintf('  finite pixels=%d/%d  min=%.4g max=%.4g\n', ...
        nnz(isfinite(A)), numel(A), min(A(isfinite(A))), max(A(isfinite(A))));

% where is the signal? compare to the analytic disc positions on a [-1,1] grid
sz = size(A,1);
xg = linspace(-1,1,sz); yg = linspace(-1,1,sz);
[XX,YY] = meshgrid(xg,yg);
B = A; B(~isfinite(B)) = 0;
m = abs(B) > 0.25*max(abs(B(:)));
fprintf('ASSUMPTION-1 quarter-amplitude set: %d px, centroid=(%.3f, %.3f)\n', ...
        nnz(m), mean(XX(m)), mean(YY(m)));
[~,k] = max(abs(B(:)));
fprintf('  peak at (x,y)=(%.3f, %.3f); expected lungs near x=+/-%.2f y=%.2f\n', ...
        XX(k), YY(k), P.lung_ctr(1), P.lung_ctr(2));

% lung-only and heart-only
[~, vh2, vi2] = p2_fwd(P, P.maxsz, E.stim, true,  false, geom);
[~, vh3, vi3] = p2_fwd(P, P.maxsz, E.stim, false, true,  geom);
L = calc_slices(inv_solve(E.imdl, vh2, vi2));
H = calc_slices(inv_solve(E.imdl, vh3, vi3));
Lb=L; Lb(~isfinite(Lb))=0;  Hb=H; Hb(~isfinite(Hb))=0;
[~,kl]=max(abs(Lb(:))); [~,kh]=max(abs(Hb(:)));
fprintf('ASSUMPTION-3 lung-only peak (%.3f, %.3f) | heart-only peak (%.3f, %.3f)\n', ...
        XX(kl), YY(kl), XX(kh), YY(kh));
fprintf('  lung-only range [%.4g %.4g]  heart-only range [%.4g %.4g]\n', ...
        min(Lb(:)), max(Lb(:)), min(Hb(:)), max(Hb(:)));
fprintf('DONE\n');
