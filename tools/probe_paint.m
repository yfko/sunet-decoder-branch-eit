% Timing + assumption probe for the painted-inclusion pipeline.
here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));
P = p2_config();
stim = mk_stim_patterns(P.n_elecs,1,[0,1],[0,1],{'no_meas_current'},1);

% --- one-time plain mesh at a FINER size than GREIT's (inverse-crime guard)
for maxsz = [0.15 0.10]
    t=tic; fm = ng_mk_cyl_models([2,2,maxsz],[P.n_elecs,1],[0.1]); tb=toc(t);
    fm.stimulation = stim;
    fprintf('mesh maxsz=%.2f: %.1f s, %d elems, %d nodes\n', ...
            maxsz, tb, size(fm.elems,1), size(fm.nodes,1));
    img = mk_image(fm,1);
    t=tic; vh = fwd_solve(img); tf=toc(t);
    fprintf('   fwd_solve: %.2f s, %d meas\n', tf, numel(vh.meas));
    if maxsz==0.15, FM=fm; IMG=img; VH=vh; end
end

E = p2_build_env(P, fullfile(here,'results','p2_env.mat'));
fprintf('GREIT env loaded\n');

ctr = interp_mesh(FM); zn = ctr(:,3)-1;
ell = @(c,r) sum(((ctr(:,1:2)-c)/r).^2,2) + (zn/r).^2 < 1;   % zscale=1 -> spheres

tt=tic;
for k=1:2
    rl = 0.30 + 0.30*rand;  rh = 0.10 + 0.20*rand;
    lc = P.lung_ctr;  hc = P.heart_ctr;
    iL = find(ell(lc,rl) | ell([-lc(1) lc(2)],rl));
    iH = find(ell(hc,rh));
    iL = setdiff(iL, iH);
    fprintf('sample %d: r_lung=%.3f r_heart=%.3f  lung %d el (%.2f%%), heart %d el (%.2f%%)\n', ...
        k, rl, rh, numel(iL), 100*numel(iL)/size(FM.elems,1), ...
        numel(iH), 100*numel(iH)/size(FM.elems,1));
    t=tic;
    im=IMG; im.elem_data(iL)=P.sig_lung; im.elem_data(iH)=P.sig_heart; vm=fwd_solve(im);
    im=IMG; im.elem_data(iL)=P.sig_lung;                                vl=fwd_solve(im);
    im=IMG;                              im.elem_data(iH)=P.sig_heart;  vhh=fwd_solve(im);
    tf=toc(t);
    t=tic;
    Am=calc_slices(inv_solve(E.imdl,VH,vm));
    Al=calc_slices(inv_solve(E.imdl,VH,vl));
    Ah=calc_slices(inv_solve(E.imdl,VH,vhh));
    tr=toc(t);
    fprintf('   3x fwd_solve %.2f s | 3x inv+slice %.2f s\n', tf, tr);
    if k==1
        sz=size(Am,1);
        xg=linspace(-1,1,sz); yg=linspace(-1,1,sz); [XX,YY]=meshgrid(xg,yg);
        fprintf('   ASSUMPTION-1 calc_slices size=[%s] finite=%d/%d\n', ...
                num2str(size(Am)), nnz(isfinite(Am)), numel(Am));
        B=Am; B(~isfinite(B))=0; [~,q]=max(abs(B(:)));
        fprintf('   peak(mixed) at (%.3f,%.3f); lungs expected near x=+/-%.2f\n', XX(q),YY(q),P.lung_ctr(1));
        Bl=Al; Bl(~isfinite(Bl))=0; [~,ql]=max(abs(Bl(:)));
        Bh=Ah; Bh(~isfinite(Bh))=0; [~,qh]=max(abs(Bh(:)));
        fprintf('   ASSUMPTION-3 lung-only peak (%.3f,%.3f) heart-only peak (%.3f,%.3f)\n', ...
                XX(ql),YY(ql),XX(qh),YY(qh));
        fprintf('   ranges: mixed [%.3g %.3g] lung [%.3g %.3g] heart [%.3g %.3g]\n', ...
                min(B(:)),max(B(:)),min(Bl(:)),max(Bl(:)),min(Bh(:)),max(Bh(:)));
    end
end
fprintf('\nper-sample total %.2f s -> 3600 samples = %.1f h\n', toc(tt)/2, toc(tt)/2*3600/3600);
fprintf('DONE\n');
