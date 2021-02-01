def comparar_modelo(test_data, model):
    from sklearn.metrics import mean_squared_error, mean_absolute_error
    
    return f"""
        Desvio Padrão: {test_data.std().round(2)}
        Erro Médio Absoluto: {mean_absolute_error(test_data, model).round(2)}
        Erro Médio Quadrático ao Quadrado: {np.sqrt(mean_squared_error(test_data, model)).round(2)}
        """
