#RED TIPO UNET3D

    model = Sequential()
    model.add(Conv3D(8, kernel_size=(3, 3, 3),
                        activation='relu', padding='same',
                        input_shape=(X_train.shape[1], X_train.shape[2],
                                    X_train.shape[3], X_train.shape[4])))
    model.add(Conv3D(8, kernel_size=(3, 3, 3),
                        activation='relu', padding='same'))
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(Conv3D(16, kernel_size=(3, 3, 3),
                        activation='relu', padding='same'))
    model.add(Conv3D(16, kernel_size=(3, 3, 3),
                        activation='relu', padding='same'))
    model.add(Dropout(0.5))
    model.add(MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(Conv3D(32, kernel_size=(3, 3, 3),
                        activation='relu', padding='same'))
    model.add(Conv3D(32, kernel_size=(3, 3, 3),
                        activation='relu', padding='same'))
    model.add(Dropout(0.5))
    model.add(UpSampling3D(size=(2, 2, 2)))
    model.add(Conv3D(16, kernel_size=(3, 3, 3),
                        activation='relu', padding='same'))
    model.add(Conv3D(16, kernel_size=(3, 3, 3),
                        activation='relu', padding='same'))
    model.add(UpSampling3D(size=(2, 2, 2)))
    model.add(Conv3D(8, kernel_size=(3, 3, 3),
                        activation='relu', padding='same'))
    model.add(Conv3D(8, kernel_size=(3, 3, 3),
                        activation='relu', padding='same'))
    model.add(Conv3D(2, kernel_size=(1, 1, 1),
                        activation='softmax'))
    model.add(GlobalAveragePooling3D())
    model.add(Dense(2, activation='softmax'))
