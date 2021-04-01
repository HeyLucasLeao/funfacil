from tensorflow.keras.callback import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau

checkpoint = ModelCheckpoint(path, monitor='vals_loss', verbose = 1)

early_stopping = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)

reduceLR = ReduceLROnplateau(monitor="val_loss", factor = 0.2, patience = 3, min_lr = 1e-4)
