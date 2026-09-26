function [vh, vi_m, vi_l, vi_h] = fwd_triple(P, maxsz, stim, geom)
%FWD_TRIPLE  Mixed / lung-only / heart-only from ONE mesh.
%
% Body identical to ../EIT_noise_geometry/src/p2_fwd.m, except that the mesh is
% built once and reused for all three conductivity configurations. Calling
% p2_fwd three times per geometry rebuilds the same Netgen mesh three times,
% and meshing dominates the cost: on this machine (Netgen 6.1 x86_64 under
% Rosetta 2) a single build of this phantom takes minutes, while fwd_solve on
% an existing mesh takes well under a second.
%
% Returns the homogeneous frame and the three inhomogeneous frames:
%   vh    -- background only, sigma = 1 everywhere
%   vi_m  -- lung + heart   (the network's input)
%   vi_l  -- lung only      (target 1)
%   vi_h  -- heart only     (target 2)
%
% P must supply n_elecs, sig_lung, sig_heart; geom supplies r_lung, r_heart,
% lung_ctr, heart_ctr.

if nargin >= 4 && ~isempty(geom)
    for f = fieldnames(geom).', P.(f{1}) = geom.(f{1}); end
end

lx = P.lung_ctr(1);  ly = P.lung_ctr(2);
hx = P.heart_ctr(1); hy = P.heart_ctr(2);
lungs = sprintf('solid obj1 = sphere(%.4f,%.4f,1;%.4f) or sphere(%.4f,%.4f,1;%.4f);', ...
                lx, ly, P.r_lung, -lx, ly, P.r_lung);
heart = sprintf('solid obj2 = sphere(%.4f,%.4f,1;%.4f);', hx, hy, P.r_heart);

[fmdl, midx] = ng_mk_cyl_models([2,2,maxsz],[P.n_elecs,1],[0.1], ...
                                {'obj1','obj2',[lungs heart]});
fmdl.stimulation = stim;

img = mk_image(fmdl,1);
vh  = fwd_solve(img);                       % homogeneous reference

im = img;  im.elem_data(midx{2}) = P.sig_lung;
           im.elem_data(midx{3}) = P.sig_heart;   vi_m = fwd_solve(im);

im = img;  im.elem_data(midx{2}) = P.sig_lung;    vi_l = fwd_solve(im);

im = img;  im.elem_data(midx{3}) = P.sig_heart;   vi_h = fwd_solve(im);
end
