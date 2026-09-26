function gen_thorax(N, outDir, opts)
%GEN_THORAX  Paired lung/heart EIT dataset on a REAL thoracic geometry.
%
%   gen_thorax(20, 'data/probe_thorax')                      % look at it
%   gen_thorax(20, 'data/probe_pig', struct('body','pig_23kg'))
%
% Exploratory generator for a possible third study. **This does not touch
% tools/gen_dataset.m**, which is named in the hashed preregistration of study 2
% and must stay exactly as it was when that study was registered.
%
% ---------------------------------------------------------------------------
% WHY A REAL THORAX
%
% Study 1 and study 2 use two spheres in a cylinder: six free parameters per
% sample. The SNR pilot showed a network trained on 2880 such samples learns
% that six-parameter manifold and emits a clean template whatever the input —
% a 3.7x change in input noise moved its output by 4%. Heterogeneous
% conductivity helped (mean heart DSC 0.991 -> 0.983) but the boundary and the
% organ shapes were still fixed and circular.
%
% mk_library_model gives a real adult thorax: a non-circular boundary and
% anatomically shaped lungs, from EIDORS' shape_library. Measured on
% adult_male_16el_lungs: 21257 elements, boundary x[-0.95 1.00] y[-0.65 0.68],
% lungs at mat_idx{2} and mat_idx{3}.
%
% ---------------------------------------------------------------------------
% THE HEART IS PAINTED, AND IT WINS OVERLAPS
%
% Neither adult_male_16el_lungs nor pig_23kg_16el_lungs carries a heart —
% both have background + lungs only, even though shape_library holds a heart
% contour for the pig. So the heart is painted as an ellipsoid.
%
% The gap between the lungs at the electrode plane is only 0.23 wide, while an
% anatomically-scaled heart has radius ~0.25-0.40 (heart ~12 cm across a ~30 cm
% thorax). It therefore *overlaps the lungs*, which is correct: the heart
% occupies the mediastinum and indents the left lung. The heart wins the
% overlap, following ../EIT_noise_geometry/src/p2_build_geom.m — letting the
% lungs win instead truncates the heart and turns a position sweep into a
% volume sweep.
%
% ---------------------------------------------------------------------------
% WHAT VARIES, AND WHAT STILL DOES NOT
%
% Varies: heart centre and radius, organ conductivity fields, measurement noise.
% Fixed: the boundary and the lung shapes — there is one adult in the library.
% So this is richer than two spheres but not unlimited. Real variability needs
% several bodies (adult_male, neonate, pig_23kg, lamb_newborn) or a deforming
% boundary (ng_mk_ellip_models).

if nargin < 1 || isempty(N),      N = 20;                    end
if nargin < 2 || isempty(outDir), outDir = 'data/probe_thorax'; end
if nargin < 3, opts = struct(); end

here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));

D = struct();
D.N          = N;
D.body       = getdef(opts,'body',      'adult_male');   % or 'pig_23kg'
D.r_heart_rng= getdef(opts,'r_heart_rng',[0.25 0.40]);
D.ctr_jitter = getdef(opts,'ctr_jitter', 0.08);
D.sig_lung   = getdef(opts,'sig_lung',   0.5);
D.sig_heart  = getdef(opts,'sig_heart',  2.0);
D.het_amp    = getdef(opts,'het_amp',    0.25);
D.het_modes  = getdef(opts,'het_modes',  8);
D.het_len    = getdef(opts,'het_len',    0.30);   % smaller body than the cylinder
D.snr_db     = getdef(opts,'snr_db',     40);
D.seed       = getdef(opts,'seed',       20260901);
D.imgsz      = 64;
D.created    = datestr(now,'yyyy-mm-dd HH:MM:SS'); %#ok<TNOW1,DATST>

rng(D.seed,'twister');
if ~isfolder(outDir), mkdir(outDir); end

%% ---- body, built once ---------------------------------------------------
model = sprintf('%s_16el_lungs', D.body);
t = tic;
fmdl = mk_library_model(model);
stim = mk_stim_patterns(16,1,[0,1],[0,1],{'no_meas_current'},1);
fmdl.stimulation = stim;
fprintf('%s: %d elems, built/loaded in %.1f s\n', model, size(fmdl.elems,1), toc(t));

ctr = interp_mesh(fmdl);
zc  = mean(arrayfun(@(e) mean(fmdl.nodes(e.nodes,3)), fmdl.electrode));
D.n_elems = size(fmdl.elems,1);
D.z_elec  = zc;

% lungs are every mat_idx block after the first
iLung = [];
for k = 2:numel(fmdl.mat_idx), iLung = [iLung; fmdl.mat_idx{k}]; end %#ok<AGROW>
D.frac_lung = numel(iLung)/D.n_elems;
fprintf('  lungs: %d elems (%.1f%%), electrode plane z=%.3f\n', ...
        numel(iLung), 100*D.frac_lung, zc);

% mediastinal centre: the background between the lungs at the electrode plane
slab = abs(ctr(:,3)-zc) < 0.04;
bg = true(D.n_elems,1); bg(iLung) = false;
xin = [max(ctr(intersect(fmdl.mat_idx{2}, find(slab)),1)), ...
       min(ctr(intersect(fmdl.mat_idx{3}, find(slab)),1))];
D.med_ctr = [mean(sort(xin)), mean(ctr(bg & slab,2))];
fprintf('  mediastinum centred near (%.3f, %.3f)\n', D.med_ctr);

%% ---- GREIT for THIS body (the cylinder cache does not apply) ------------
cacheF = fullfile(here,'results', sprintf('greit_%s.mat', D.body));
if isfile(cacheF)
    S = load(cacheF); imdl = S.imdl;
    fprintf('  GREIT model: loaded cache\n');
else
    t = tic;
    fmdlG = mk_library_model(model);
    fmdlG.stimulation = stim;  fmdlG = mdl_normalize(fmdlG,1);
    rng(4242);   % distr 2 draws training targets at random
    imdl = mk_GREIT_model(mk_image(fmdlG,1), 0.2, [], ...
        struct('imgsz',[D.imgsz D.imgsz],'distr',2,'Nsim',1000, ...
               'target_size',0.02,'noise_figure',0.5));
    if ~isfolder(fileparts(cacheF)), mkdir(fileparts(cacheF)); end
    save(cacheF,'imdl','-v7.3');
    fprintf('  GREIT model: built in %.1f min\n', toc(t)/60);
end

img0 = mk_image(fmdl,1);
vh   = fwd_solve(img0);          % homogeneous reference, geometry-independent

%% ---- generate ----------------------------------------------------------
recon_mixed = nan(D.imgsz,D.imgsz,N);
recon_lung  = nan(D.imgsz,D.imgsz,N);
recon_heart = nan(D.imgsz,D.imgsz,N);
ok = false(1,N);
G = struct('r_heart',{},'heart_ctr',{},'frac_heart',{},'overlap',{});

t0 = tic;
for i = 1:N
    g = struct();
    g.r_heart   = urand(D.r_heart_rng);
    g.heart_ctr = D.med_ctr + D.ctr_jitter*(2*rand(1,2)-1);
    try
        d = [(ctr(:,1)-g.heart_ctr(1))/g.r_heart, ...
             (ctr(:,2)-g.heart_ctr(2))/g.r_heart, ...
             (ctr(:,3)-zc)/(g.r_heart*2.0)];      % elongated in z, as anatomy is
        iH = find(sum(d.^2,2) < 1);
        % heart wins the overlap
        g.overlap = numel(intersect(iH, iLung));
        iL = setdiff(iLung, iH);
        g.frac_heart = numel(iH)/D.n_elems;
        if isempty(iH) || isempty(iL), error('gen:empty','empty inclusion'); end

        if D.het_amp > 0
            rsH = RandStream('threefry','Seed', D.seed + 7919*i);
            sL = D.sig_lung *(1 + D.het_amp*smooth_field(ctr(iL,:),D.het_modes,D.het_len,rsH));
            sH = D.sig_heart*(1 + D.het_amp*smooth_field(ctr(iH,:),D.het_modes,D.het_len,rsH));
            sL = max(sL,0.05); sH = max(sH,0.05);
        else
            sL = D.sig_lung; sH = D.sig_heart;
        end

        im = img0; im.elem_data(iL)=sL; im.elem_data(iH)=sH; vi_m = fwd_solve(im);
        im = img0; im.elem_data(iL)=sL;                      vi_l = fwd_solve(im);
        im = img0;                      im.elem_data(iH)=sH; vi_h = fwd_solve(im);

        if ~isempty(D.snr_db)
            vi_m = p2_add_noise(vi_m, vh, D.snr_db, D.seed + 104729*i);
        end
        recon_mixed(:,:,i) = slice64(inv_solve(imdl, vh, vi_m), D.imgsz);
        recon_lung (:,:,i) = slice64(inv_solve(imdl, vh, vi_l), D.imgsz);
        recon_heart(:,:,i) = slice64(inv_solve(imdl, vh, vi_h), D.imgsz);
        ok(i) = true;
    catch ME
        warning('sample %d failed (%s)', i, ME.message);
    end
    G(i) = g;
    if mod(i,10)==0
        e=toc(t0); fprintf('  %4d/%d  %.2f s/sample  eta %.1f min\n', i, N, e/i, (e/i)*(N-i)/60);
    end
end
fprintf('generated %d/%d in %.1f min\n', nnz(ok), N, toc(t0)/60);

D.geom = G; D.ok = ok;
save(fullfile(outDir,'dataset.mat'), 'recon_mixed','recon_lung','recon_heart','D','-v7.3');

fid = fopen(fullfile(outDir,'PROVENANCE.txt'),'w');
fprintf(fid,'created      %s\n', D.created);
fprintf(fid,'body         %s (%s), %d elems\n', D.body, model, D.n_elems);
fprintf(fid,'N            %d generated of %d\n', nnz(ok), N);
fprintf(fid,'lungs        anatomical, fixed shape, %.1f%% of mesh\n', 100*D.frac_lung);
fprintf(fid,'heart        painted ellipsoid, r %.2f-%.2f, jitter %.2f, wins overlap\n', ...
        D.r_heart_rng, D.ctr_jitter);
fprintf(fid,'  mean frac  %.4f, mean overlap %.0f elems\n', ...
        mean([G(ok).frac_heart]), mean([G(ok).overlap]));
fprintf(fid,'organ sigma  heterogeneous amp %.2f, %d modes, len %.2f\n', ...
        D.het_amp, D.het_modes, D.het_len);
fprintf(fid,'noise        %g dB on mixed input only\n', D.snr_db);
fprintf(fid,'GREIT        built for this body, imgsz [%d %d]\n', D.imgsz, D.imgsz);
fclose(fid);
fprintf('wrote %s\n', fullfile(outDir,'dataset.mat'));
end

% -------------------------------------------------------------------------
function v = getdef(s,f,d)
if isfield(s,f) && ~isempty(s.(f)), v = s.(f); else, v = d; end
end
function x = urand(r), x = r(1) + (r(2)-r(1))*rand; end
function v = smooth_field(pts,n,len,rs)
v = zeros(size(pts,1),1);
for k = 1:n
    dir = randn(rs,1,3); dir = dir/norm(dir);
    lam = len*(0.5+rand(rs)); ph = 2*pi*rand(rs);
    v = v + sin(pts*dir'*(2*pi/lam) + ph);
end
v = v/sqrt(n);
end
function A = slice64(img, sz)
img.calc_colours.ref_level = 0;
A = reshape(calc_slices(img), sz, sz);
end
