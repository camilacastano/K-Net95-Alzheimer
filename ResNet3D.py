#RED TIPO RESNET3D

    model = Sequential()
    model.add(Conv3D(8, kernel_size=(3, 3, 3), strides=(1, 1, 1),
                        activation='relu', padding='same',
                        input_shape=(X_train.shape[1],
                                    X_train.shape[2],
                                    X_train.shape[3],
                                    X_train.shape[4])))
    model.add(BatchNormalization(center=True, scale=True))
    model.add(Conv3D(8, kernel_size=(3, 3, 3), strides=(2, 2, 2),
                        activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv3D(8, kernel_size=(3, 3, 3), strides=(1, 1, 1),
                        activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv3D(16, kernel_size=(3, 3, 3), strides=(2, 2, 2),
                        activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv3D(16, kernel_size=(3, 3, 3), strides=(1, 1, 1),
                        activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv3D(32, kernel_size=(3, 3, 3), strides=(2, 2, 2),
                        activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv3D(32, kernel_size=(3, 3, 3), strides=(1, 1, 1),
                        activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv3D(64, kernel_size=(3, 3, 3), strides=(2, 2, 2),
                        activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv3D(64, kernel_size=(3, 3, 3), strides=(1, 1, 1),
                        activation='relu', padding='same'))#512 x 64
    model.add(BatchNormalization())
    model.add(GlobalAveragePooling3D())
    model.add(Dense(2, activation='softmax'))
