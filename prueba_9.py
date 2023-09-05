#PRUEBA 9

model = Sequential()
model.add(Conv3D(32, kernel_size=(3, 3, 3),
                        activation='relu',
                        kernel_initializer='he_uniform', 
                        input_shape=(X_train.shape[1], X_train.shape[2], 
                                     X_train.shape[3], X_train.shape[4])))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.5))
model.add(Conv3D(8, kernel_size=(3, 3, 3), activation='relu', 
                        kernel_initializer='he_uniform'))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.5))
model.add(Conv3D(4, kernel_size=(3, 3, 3), activation='relu', 
                        kernel_initializer='he_uniform'))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.5))
model.add(Conv3D(2, kernel_size=(3, 3, 3), activation='relu', 
                        kernel_initializer='he_uniform'))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.4))
model.add(Flatten())
model.add(Dense(1024, activation=LeakyReLU(alpha=0.01), 
                    kernel_initializer='he_uniform',
                    kernel_regularizer=regularizers.L2(0.01)))
model.add(Dropout(0.6))
model.add(Dense(512, activation=LeakyReLU(alpha=0.01), 
                    kernel_initializer='he_uniform',
                    kernel_regularizer=regularizers.L2(0.01)))
model.add(Dropout(0.7))
model.add(Dense(128, activation=LeakyReLU(alpha=0.01), 
                    kernel_initializer='he_uniform',
                    kernel_regularizer=regularizers.L2(0.01)))
model.add(Dropout(0.6))
model.add(Dense(2, activation='softmax'))
