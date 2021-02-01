def plot_forecast(train_data, test_data, model, figsize=(12,8), interval=None):
    %matplotlib inline
    train_data.plot(legend=True, label = 'TRAIN', figsize=figsize)
    test_data.plot(legend=True, label = 'TEST', figsize=figsize)
    model.plot(legend=True, label = 'PREDICT', figsize=figsize, xlim=interval)
