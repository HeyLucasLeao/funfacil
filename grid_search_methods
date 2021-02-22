list_of_smape = []

for i in range(1, 100):
    regressor = KNeighborsRegressor(metric='manhattan', n_neighbors = i)
    reduced_reg = ReducedForecaster(scitype ='regressor',regressor = regressor, window_length= 7)
    reduced_reg.fit(train_scaled)
    y_pred = reduced_reg.predict(fh)
    list_of_smape.append([smape_loss(test_scaled, y_pred), i])
    
