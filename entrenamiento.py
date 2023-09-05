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
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv3D, MaxPooling3D, BatchNormalization, Dropout, Flatten, Dense, GlobalAveragePooling3D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.layers import LeakyReLU
from keras import regularizers
from tensorflow.keras.models import load_model

def array_to_color(array, cmap="Oranges"):
    s_m = plt.cm.ScalarMappable(cmap=cmap)
    return s_m.to_rgba(array)[:,:-1]

def recortar(data):
    return data[:,40:215,12:220,40:215,:]

def rgb_data_transform(data):
    data_t = []
    for i in range(data.shape[0]):
        data_t.append(array_to_color(data[i]).reshape(16, 16, 16, 3))
    return np.asarray(data_t, dtype=np.float32)


folder_path3 = MCI_data
folder_path2 = CN_data
folder_path = AD_data


datanp = np.zeros((1, 256, 256, 256, 1))
truenp = [0]



for filename in os.listdir(folder_path):
    if filename.endswith('.nii') or filename.endswith('.nii.gz'):
        file_path = os.path.join(folder_path, filename)
        datanp2 = nib.load(file_path).get_fdata()
        datanp = np.append(datanp, datanp2)
        truenp = np.append(truenp, [0])

for filename in os.listdir(folder_path2):
    if filename.endswith('.nii') or filename.endswith('.nii.gz'):
        file_path = os.path.join(folder_path2, filename)
        datanp2 = nib.load(file_path).get_fdata()
        datanp = np.append(datanp, datanp2)
        truenp = np.append(truenp, [1])

truenp = np.delete(truenp, 0)
datanp = datanp.reshape(truenp.shape[0]+1, 256, 256, 256, 1)
datanp = np.delete(datanp, 0, axis=0)

datanp = recortar(datanp)

X_train, X_test, y_train, y_test = train_test_split(datanp, truenp, test_size=0.3, shuffle=True, stratify=truenp, random_state=42)

# Cargar el modelo desde un archivo .h5
loaded_model = load_model('modeloalexsito3.h5')
loaded_model.summary()

# Preprocesar los datos de entrenamiento
y_train_categorical = to_categorical(y_train, 2)
y_test_categorical = to_categorical(y_test, 2)

# Compilar el modelo cargado
loaded_model.compile(loss='binary_crossentropy',
                     optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
                     metrics=['accuracy'])

# Definir la ruta donde se guardarán los puntos de control
checkpoint_dir = entrenamiento.ckpt

# Definir el callback ModelCheckpoint
checkpoint = ModelCheckpoint("K-Net95o.h5", monitor='val_loss', verbose=1, save_weights_only=False, save_best_only=True, mode='auto')


# Entrenar el modelo cargado
new_history = loaded_model.fit(X_train, y_train_categorical,
                               batch_size=10,
                               epochs=100,
                               verbose='auto',
                               validation_split=0.3,
                               callbacks=[checkpoint])

# Guardar el modelo completo
loaded_model.save(os.path.join(checkpoint_dir, "K-Net95oo.h5"))

score = loaded_model.evaluate(X_test, y_test_categorical)
print('\n', 'Test accuracy:', score[1])

# Evaluar el modelo cargado en el conjunto de datos de prueba
loss, accuracy = loaded_model.evaluate(X_test, y_test_categorical)
print("Precisión en el conjunto de datos de prueba:", accuracy)

#visulaización de resultados (curvas de aprendizaje)
plt.plot(new_history.history['accuracy'])
plt.plot(new_history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

plt.plot(new_history.history['loss'])
plt.plot(new_history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

pd.DataFrame(new_history.history).plot(figsize=(8,5))
plt.show()
