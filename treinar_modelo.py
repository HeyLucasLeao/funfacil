def treinar_modelo(params):
    SEED = 4

    learning_rate = params[0]
    num_leaves = params[1]
    min_child_samples = params[2]
    subsample = params[3]
    colsample_bytree = params[4]
    n_estimators = params[5]

    print(params, '\n')
    
    fh = np.arange(1, len(y_test) + 1)
    mdl = LGBMRegressor(random_state=SEED,
    learning_rate = learning_rate, 
    num_leaves = num_leaves, 
    min_child_samples = min_child_samples, 
    subsample = subsample,
    colsample_bytree = colsample_bytree,
    subsample_freq=1,
    n_estimators=n_estimators)
    reg = RecursiveRegressionForecaster(regressor = mdl, window_length= 7)
    reg.fit(y_train)
    y_pred = reg.predict(fh)

    return smape_loss(y_test, y_pred)

space = [(1e-3, 1e-1, 'log-uniform'), #learning rate
(2, 128), #num_leaves
(1, 100), #min_child_samples
(0.05, 1.0), #subsample
(0.1, 1.0), #colsample_bytree
(100, 1000)] #n_estimators

result = dummy_minimize(treinar_modelo, 
space,
random_state=SEED, 
verbose=1,
n_calls = 30)
