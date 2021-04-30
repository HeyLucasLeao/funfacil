from sktime.performance_metrics.forecasting import smape_loss


def expanding_window_splitter(data_frame, target, model, fh=1, step_length=1, initial_window = 10, SEED = 4):
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
