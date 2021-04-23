from lightgbm import LGBMRegressor
from sktime.performance_metrics.forecasting import smape_loss


def ExpandingWindowSplitter(data_frame, target, fh=1, step_length=1, initial_window = 10, SEED = 4):
    model = LGBMRegressor(random_state=SEED,
    learning_rate=0.1,
    colsample_bytree=0.19578750056100663,
    min_child_samples=78,
    n_estimators=666, num_leaves=104,
    subsample=1.0,
    subsample_freq=1)

    data_frame = data_frame.copy()
    data_frame = data_frame.drop(columns=['date'])

    X_data = data_frame.drop(columns=[target])
    y_data = data_frame[target]
    
    data_frame['test_sMAPE'] = np.nan

    for i in range(initial_window, len(data_frame), step_length):

        X_train, X_test = X_data[:i], X_data[i:i + fh]
        y_train, y_test = y_data[:i], y_data[i:i + fh]

        model.fit(X_train, y_train)

        y_pred = pd.Series(model.predict(X_test), index=y_test.index)

        res = smape_loss(y_test, y_pred)

        data_frame['test_sMAPE'].loc[i:i + fh] = res

    return data_frame
