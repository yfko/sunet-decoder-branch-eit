% SNR pilot for PREREGISTRATION_HEART.md s7.
% Generates a small dataset at each candidate SNR. Trains nothing, compares
% nothing -- its only job is to let the selection rule pick the primary SNR.
% NOTE: MATLAB's run() cd's into the script's own folder, so every path here
% must be absolute -- a relative outDir would land in tools/, not the project.
here = fileparts(fileparts(mfilename('fullpath')));
addpath(fullfile(here,'tools'));
cd(here);
levels = [15 10];
for k = 1:numel(levels)
    s = levels(k);
    fprintf('\n===== SNR %d dB =====\n', s);
    gen_dataset(300, fullfile(here, sprintf('data/pilot_snr%02d', s)), ...
                struct('snr_db', s, 'seed', 20260829, 'ctr_jitter', 0.05));
end
fprintf('\nPILOT DATA DONE\n');
