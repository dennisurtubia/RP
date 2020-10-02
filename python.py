import numpy as np
import json
import mne
import scipy
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from scipy.signal import stft

data = np.load('files/data.npy')
labels = np.load('files/labels.npy')

desc_file = open('files/deor.json')
deor = json.loads(desc_file.read())
desc_file.close()

print('Estruturas => dados', data.shape, 'labels', labels.shape)
print(labels)

data = data[:,:256,:]

trial_duration = 5
sampling_frequency = data.shape[-1] / trial_duration
montage = mne.channels.make_standard_montage('EGI_256')
ch_names = data.shape[1]
ch_types = 'eeg'

# primeiramente devemos criar o objeto info
info = mne.create_info(montage.ch_names, sampling_frequency, ch_types)

#set experiments montage
info.set_montage(montage)

# por fim a criação do EpochsArray
events = np.array([[index, 0, event] for index, event in enumerate(labels)])
#objeto MNE epoch
epoch = mne.EpochsArray(data, info, events)

filtered_epoch = epoch.copy().pick_channels(['E118', 'E125', 'E110', 'E116', 'E119', 'E126', 'E150', 'E152'])
filtered_epoch.filter(l_freq = 5.0, h_freq = 14.0)
# CAR
# mne.set_eeg_reference(filtered_epoch, ref_channels=['E116', 'E126', 'E150','E106','E107','E108','E109','E119','E140','E151','E160','E169'])


# data = epoch.get_data()
# _, _, w = stft(data, fs=241, nperseg=32, noverlap=16)

X, _ = mne.time_frequency.psd_multitaper(filtered_epoch, fmin=5.0, fmax=14.0)
print('Shape dos dados:', X.shape)

# X = X.transpose(0, 2, 1)
X = X.reshape(X.shape[0], X.shape[1] * X.shape[2])
# features = list()
# for feature in (X):
#     feature = feature.transpose(0, 2, 1)
#     feature = feature.reshape(feature.shape[0] * feature.shape[1], feature.shape[2])
#     features.append(feature)

# # vetor de características final
# X = np.concatenate(features, axis=-1)
print('Shape dos dados:', X.shape)

y = np.load('files/labels.npy')
print('Shape original dos labels', y.shape)

# size = int(X.shape[0] / y.shape[0])
# y = np.concatenate([y for i in range(size)])
print('Shape final dos labels', y.shape)

for count in range(50):
    for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
        for gamma in [10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]:
            for C in [0.01, 0.1, 1, 10, 100, 1000]:
                X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True)
                clf = SVC(gamma=gamma, kernel=kernel, C=C)
                clf.fit(X_train, y_train)
                res = clf.predict(X_test)
                tot_hit = sum([1 for i in range(len(res)) if res[i] == y_test[i]])
                if tot_hit / X_test.shape[0] * 100 > 50:
                    print('Acurácia: {:.2f}%'.format(tot_hit / X_test.shape[0] * 100))

