def train_test_split_AR(data, percent=0.33):
    divide = 1 - percent
    train_size = int(len(data) * divide)
    data_train = data[:train_size]
    data_test = data[train_size:]
    return (data_train, data_test)
