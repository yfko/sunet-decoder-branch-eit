% Explore what a realistic thoracic model gives us, for study 3.
here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'..','EIT_noise_geometry','src'));

fprintf('=== shape_library 內容 ===\n');
S = load(fullfile(fileparts(which('mk_library_model')),'shape_library.mat'));
f = fieldnames(S);
for i=1:numel(f)
    v = S.(f{i});
    if isstruct(v)
        fprintf('  %-24s : %s\n', f{i}, strjoin(fieldnames(v)', ', '));
    else
        fprintf('  %-24s : %s %s\n', f{i}, class(v), mat2str(size(v)));
    end
end

fprintf('\n=== 建 adult_male_16el_lungs ===\n');
t=tic; fmdl = mk_library_model('adult_male_16el_lungs'); tb=toc(t);
fprintf('  建模 %.1f s\n', tb);
fprintf('  節點 %d, 元素 %d, 電極 %d\n', size(fmdl.nodes,1), size(fmdl.elems,1), numel(fmdl.electrode));
fprintf('  mat_idx 區塊數: %d\n', numel(fmdl.mat_idx));
for i=1:numel(fmdl.mat_idx)
    fprintf('    mat_idx{%d}: %6d 元素 (%.2f%%)\n', i, numel(fmdl.mat_idx{i}), ...
            100*numel(fmdl.mat_idx{i})/size(fmdl.elems,1));
end
b = [min(fmdl.nodes); max(fmdl.nodes)];
fprintf('  邊界範圍 x[%.2f %.2f] y[%.2f %.2f] z[%.2f %.2f]\n', ...
        b(1,1),b(2,1), b(1,2),b(2,2), b(1,3),b(2,3));
zc = mean(arrayfun(@(e) mean(fmdl.nodes(e.nodes,3)), fmdl.electrode));
fprintf('  電極平面 z = %.3f\n', zc);

fprintf('\n=== 與現用圓柱體模的對比 ===\n');
P = p2_config();
fprintf('  圓柱: 半徑 2, 高 2, 兩顆肺球 + 一顆心球, 6 個自由參數\n');
fprintf('  胸腔: 真實邊界形狀 + 解剖肺形狀, mat_idx 提供器官索引\n');
fprintf('\nDONE\n');
