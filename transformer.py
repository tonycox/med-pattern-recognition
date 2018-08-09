import mne.io

eeg_fname = './dataset/record_1.eeg'
edf_fname = './dataset/record_1.edf'

read_edf = mne.io.read_raw_edf(edf_fname)
# read_eeg = mne.io.read_raw_eximia(eeg_fname)
print(read_edf)
# print(read_eeg)
