% Where can a heart be painted, and what does the pig model give for free?
for name = {'adult_male_16el_lungs','pig_23kg_16el_lungs'}
    nm = name{1};
    fprintf('\n========== %s ==========\n', nm);
    fmdl = mk_library_model(nm);
    ctr = interp_mesh(fmdl); zc = mean(arrayfun(@(e) mean(fmdl.nodes(e.nodes,3)), fmdl.electrode));
    fprintf('元素 %d, 電極平面 z=%.3f, mat_idx 區塊 %d\n', ...
            size(fmdl.elems,1), zc, numel(fmdl.mat_idx));
    for i=1:numel(fmdl.mat_idx)
        c = ctr(fmdl.mat_idx{i},:);
        fprintf('  mat_idx{%d} %6d 元素  質心 (%6.3f,%6.3f,%6.3f)  x[%.2f %.2f] y[%.2f %.2f]\n', ...
            i, numel(fmdl.mat_idx{i}), mean(c(1,:)*0+mean(c,1)), ...
            min(c(:,1)),max(c(:,1)), min(c(:,2)),max(c(:,2)));
    end
    % 縱膈空間：電極平面附近、不屬於任何器官的背景
    slab = abs(ctr(:,3)-zc) < 0.05;
    organs = false(size(ctr,1),1);
    for i=2:numel(fmdl.mat_idx), organs(fmdl.mat_idx{i}) = true; end
    gap = slab & ~organs;
    g = ctr(gap,:);
    fprintf('  電極平面附近的非器官背景: %d 元素\n', nnz(gap));
    if nnz(gap)>0
        fprintf('    x[%.2f %.2f]  y[%.2f %.2f]  質心 (%.3f, %.3f)\n', ...
                min(g(:,1)),max(g(:,1)), min(g(:,2)),max(g(:,2)), mean(g(:,1)), mean(g(:,2)));
    end
end
fprintf('\nDONE\n');
