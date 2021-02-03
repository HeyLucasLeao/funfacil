def plot_forecast(training_set, test_set, model=None, figsize=(12,8), interval=None):
    %matplotlib inline
    training_set.plot(legend=True, label = 'TRAIN', figsize=figsize)
    test_set.plot(legend=True, label = 'TEST', figsize=figsize)
    model.plot(legend=True, label = 'PREDICT', figsize=figsize, xlim=interval)
