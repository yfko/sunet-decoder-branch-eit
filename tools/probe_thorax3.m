fmdl = mk_library_model('adult_male_16el_lungs');
ctr = interp_mesh(fmdl);
zc  = mean(arrayfun(@(e) mean(fmdl.nodes(e.nodes,3)), fmdl.electrode));
slab = abs(ctr(:,3)-zc) < 0.04;              % 電極平面薄片

lab = {'background','lung A','lung B'};
for i=1:3
    m = false(size(ctr,1),1); m(fmdl.mat_idx{i}) = true; m = m & slab;
    c = ctr(m,:);
    fprintf('%-11s %5d 元素  質心 (%+.3f, %+.3f)  x[%+.2f %+.2f] y[%+.2f %+.2f]\n', ...
        lab{i}, nnz(m), mean(c(:,1)), mean(c(:,2)), ...
        min(c(:,1)), max(c(:,1)), min(c(:,2)), max(c(:,2)));
end

% 兩肺之間的縱膈：背景元素中，x 介於兩肺內緣之間的部分
bg = false(size(ctr,1),1); bg(fmdl.mat_idx{1}) = true; bg = bg & slab;
L2 = false(size(ctr,1),1); L2(fmdl.mat_idx{2}) = true; L2 = L2 & slab;
L3 = false(size(ctr,1),1); L3(fmdl.mat_idx{3}) = true; L3 = L3 & slab;
xin = [max(ctr(L2,1)) min(ctr(L3,1))];       % 可能左右相反，取交集區間
lo = min(xin); hi = max(xin);
med = bg & ctr(:,1)>lo & ctr(:,1)<hi;
c = ctr(med,:);
fprintf('\n縱膈候選區（兩肺內緣之間的背景）: %d 元素\n', nnz(med));
fprintf('  x[%+.3f %+.3f]  y[%+.3f %+.3f]  質心 (%+.3f, %+.3f)\n', ...
    min(c(:,1)),max(c(:,1)), min(c(:,2)),max(c(:,2)), mean(c(:,1)), mean(c(:,2)));
fprintf('  可容納的最大內切半徑約 %.3f\n', min([ (max(c(:,1))-min(c(:,1)))/2, (max(c(:,2))-min(c(:,2)))/2 ]));
fprintf('\n體模尺度參考: 邊界 x[%.2f %.2f] y[%.2f %.2f]\n', ...
    min(fmdl.nodes(:,1)),max(fmdl.nodes(:,1)),min(fmdl.nodes(:,2)),max(fmdl.nodes(:,2)));
fprintf('DONE\n');
