import numpy as np
from sktime.forecasting.compose import ReducedForecaster

def grid_search_ts_algorithms(y_train, y_test, algorithms=[], feature_range=(1, 100), window_length = 7):
    fh = np.arange(1, len(y_test) + 1)
    list_of_algorithms = algorithms
    list_of_smape = []

    for i in range(feature_range):
        for algorithm in list_of_algorithms:
            reduced_reg = ReducedForecaster(scitype ='regressor',regressor = algorithm, window_length= window_length)
            reduced_reg.fit(y_train)
            y_pred = reduced_reg.predict(fh)
            list_of_smape.append([smape_loss(y_test, y_pred), i])
    return min(list_of_smape)
