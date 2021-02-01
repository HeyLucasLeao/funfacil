def plot_forecast(train_data, test_data, model):
    %matplotlib inline
    train_data.plot(legend=True, label = 'TRAIN', figsize=(12,8))
    test_data.plot(legend=True, label = 'TEST', figsize=(12,8))
    model.plot(legend=True, label = 'PREDICT', figsize=(12,8))
