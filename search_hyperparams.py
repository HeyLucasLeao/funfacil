def search_hyperparams(params):
    SEED = 4

    learning_rate = params[0]
    num_leaves = params[1]
    min_child_samples = params[2]
    subsample = params[3]
    colsample_bytree = params[4]
    n_estimators = params[5]

    print(params, '\n')
    
    mdl = LGBMClassifier(random_state=SEED,
    learning_rate = learning_rate, 
    num_leaves = num_leaves, 
    min_child_samples = min_child_samples, 
    subsample = subsample,
    colsample_bytree = colsample_bytree,
    subsample_freq=1,
    n_estimators=n_estimators)
    mdl.fit(X_train, y_train)
    y_pred = mdl.predict(X_test)

    return -accuracy_score(y_test, y_pred)

space = [(1e-3, 1e-1, 'log-uniform'), #learning rate
(2, 128), #num_leaves
(1, 100), #min_child_samples
(0.05, 1.0), #subsample
(0.1, 1.0), #colsample_bytree
(100, 1000)] #n_estimators

result = dummy_minimize(search_hyperparams, 
space,
random_state=SEED, 
verbose=1,
n_calls = 30)

#learning_rate, num_leaves, min_child_samples, subsample, colsample_bytree, n_estimators = result.x
