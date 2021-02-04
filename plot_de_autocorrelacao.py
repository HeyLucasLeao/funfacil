def plot_de_autocorrelacao(data, figsize=(12,6), lags = 40, zero = False, title="", method= 'ywadjusted'):
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    import matplotlib.pyplot as plt    
    
    plot_acf(data, lags = lags, zero = zero)
    plt.title("Autocorrelação" + " "+ title)
    plt.show()
    plot_pacf(data, lags = lags, zero = zero, method= method)
    plt.title("Autocorrelação Parcial" + " "+ title)
    plt.show()
