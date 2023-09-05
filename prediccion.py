import os
import h5py
from keras.utils import to_categorical
import numpy as np
from numpy import append
import matplotlib.pyplot as plt
import pandas as pd
import nibabel as nib
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras   
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.layers import LeakyReLU
from keras import regularizers
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.layers import LeakyReLU
from keras import regularizers
from skimage.transform import resize
import matplotlib.gridspec as gridspec

Knet95_model = load_model('K-Net95.h5')

folder_path3= mci_mci_data #mci
folder_path4= normal_ad #Late mci
folder_path5= normal_mci #early mci

Xmci=np.zeros((1, 175, 208, 175,1))   #images
true_index=['nada']

#cargamos arreglo con datos de mci
for filename in os.listdir(folder_path3):
  if filename.endswith('.nii') or filename.endswith('.nii.gz'):
    file_path = os.path.join(folder_path3, filename)

    datanp2=nib.load(file_path).get_fdata()
    datanp2=resize(datanp2, (175, 208, 175), mode='constant', anti_aliasing=True)
    Xmci=np.append(Xmci,datanp2)
    true_index=np.append(true_index,['NC'])

#cargamos arreglo con datos de late
for filename in os.listdir(folder_path4):
  if filename.endswith('.nii') or filename.endswith('.nii.gz'):
    file_path = os.path.join(folder_path4, filename)

    datanp2=nib.load(file_path).get_fdata()
    datanp2=resize(datanp2, (175, 208, 175), mode='constant', anti_aliasing=True)
    Xmci=np.append(Xmci,datanp2)
    true_index=np.append(true_index,['AD'])


#cargamos arreglo con datos de early
for filename in os.listdir(folder_path5):
  if filename.endswith('.nii') or filename.endswith('.nii.gz'):
    file_path = os.path.join(folder_path5, filename)

    datanp2=nib.load(file_path).get_fdata()
    datanp2=resize(datanp2, (175, 208, 175), mode='constant', anti_aliasing=True)
    Xmci=np.append(Xmci,datanp2)
    true_index=np.append(true_index,['CN'])

#eliminamos primer elemento de ceros
true_index = np.delete(true_index, 0) #ojo, solo ejecutar una vez
Xmci = Xmci.reshape(true_index.shape[0]+1,175, 208, 175,1)
Xmci = np.delete(Xmci,0, axis=0) 

# EXPERIMENTO 4
y_hat = Knet95_model.predict(Xmci)

corte=110
# Tamaño de la figura
figure = plt.figure(figsize=(30, 10))

# Configurar las proporciones de los subgráficos
gs = gridspec.GridSpec(1, 5, width_ratios=[12, 12, 12, 12, 12])

for i, index in enumerate(np.random.choice(Xmci.shape[0], size=5)):
    ax = plt.subplot(gs[i])
    # Resto del código para cada subgráfico
    plt.imshow(Xmci[index, :, :, corte], cmap='bone')
    predict_index = np.argmax(y_hat[index])
    ax.set_title("{}".format('Alzheimer Disease' if predict_index == 0 else 'Cognitive Normal'))
    ax.set_xticks([])
    ax.set_yticks([])
    plt.text(20, 15, f'Prob. de Alzheimer ~{round(y_hat[index, 0] * 100, 3)}%', color='white', fontsize=10)

plt.subplots_adjust(wspace=0.5, hspace=0.5)  # Ajustar el espaciado de los subgráficos
plt.show()  # Mostrar la figura
