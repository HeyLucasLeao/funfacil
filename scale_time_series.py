# scale train and test data to [-1, 1]
def scale_time_series(train, test):
    # fit scaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler = scaler.fit(np.array(train).reshape(-1,1))
    # transform train
    train = np.array(train).reshape(-1,1)
    train_scaled = scaler.transform(train)
    train_scaled = pd.Series(np.concatenate(train_scaled))
    # transform test
    test = np.array(test).reshape(-1,1)
    test_scaled = scaler.transform(test)
    test_scaled = pd.Series(np.concatenate(test_scaled))
    test_scaled.index = pd.RangeIndex(start= train_scaled.tail(1).index.values[0] + 1,
                                     stop=train_scaled.tail(1).index.values[0] + len(test_scaled) + 1)
    return scaler, train_scaled, test_scaled
