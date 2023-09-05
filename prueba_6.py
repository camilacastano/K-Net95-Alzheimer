#PRUEBA 6

model = Sequential()
model.add(Conv3D(16, kernel_size=(3, 3, 3),
                        activation='relu',
                        kernel_initializer='he_uniform', 
                        input_shape=(X_train.shape[1], 
                        X_train.shape[2], 
                        X_train.shape[3],
                        X_train.shape[4])))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.7))
model.add(Conv3D(8, kernel_size=(3, 3, 3), activation='relu', 
                        kernel_initializer='he_uniform', 
                        kernel_regularizer=regularizers.L2(0.01)))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.7))
model.add(Conv3D(4, kernel_size=(3, 3, 3), activation='relu', 
                        kernel_initializer='he_uniform', 
                        kernel_regularizer=regularizers.L2(0.01)))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.5))
model.add(Conv3D(2, kernel_size=(3, 3, 3), activation='relu', 
                        kernel_initializer='he_uniform', 
                        kernel_regularizer=regularizers.L2(0.01)))
model.add(MaxPooling3D(pool_size=(2, 2, 2)))
model.add(BatchNormalization(center=True, scale=True))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(30, activation='sigmoid',
                        kernel_initializer='he_uniform'))
model.add(Dense(30, activation='relu',
                        kernel_initializer='he_uniform'))
model.add(Dense(2, activation='softmax'))
