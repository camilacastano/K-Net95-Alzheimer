#RED FINAL

model = Sequential()
model.add(Conv3D(32, kernel_size=(3, 3, 3),
                         activation='relu',
                         kernel_initializer='he_uniform',
                         kernel_regularizer=regularizers.L2(0.001),
                         input_shape=(X_train.shape[1], X_train.shape[2],
                                      X_train.shape[3], X_train.shape[4])))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.4))
model.add(Conv3D(16, kernel_size=(3, 3, 3), activation='relu',
                         kernel_initializer='he_uniform',
                         kernel_regularizer=regularizers.L2(0.001)))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.4))
model.add(Conv3D(8, kernel_size=(3, 3, 3), activation='relu',
                        kernel_initializer='he_uniform'))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.3))
model.add(Conv3D(8, kernel_size=(3, 3, 3), activation='relu',
                        kernel_initializer='he_uniform'))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(512, activation=LeakyReLU(alpha=0.01),
                         kernel_initializer='he_uniform',
                         kernel_regularizer=regularizers.L2(0.001)))
model.add(Dropout(0.1))
model.add(Dense(128, activation=LeakyReLU(alpha=0.01),
                         kernel_initializer='he_uniform',
                         kernel_regularizer=regularizers.L2(0.001)))
model.add(Dropout(0.1))
model.add(Dense(2, activation='softmax'))


# Esta es la estructura modificada final utilizada para la etapa de prueba.
# Cabe destacar que el nombre de esta red fue escogido en honor a Kendrick Lamar y su cancion N95!!
