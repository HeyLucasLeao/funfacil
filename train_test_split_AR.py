def train_test_split_AR(data, percentage_to_test=0.33):
    divide = 1 - percentage_to_test
    train_size = int(len(data) * divide)
    training_set = data[:train_size + 1]
    test_set = data[train_size:]
    return (training_set, test_set)
