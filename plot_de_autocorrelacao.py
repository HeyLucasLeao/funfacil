def plot_de_autocorrelacao(data, title='Correlação de Dados', figsize=(12,6), lags = 40, zero = False):
    from pandas.plotting import autocorrelation_plot
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    import matplotlib.pyplot as plt    
    ax1 = plt.figure(figsize=figsize)
    ax1.suptitle(title, fontsize=18, x= 0.26, y= 0.95)
    autocorrelation_plot(data)
    
    plot_acf(data, lags = lags, zero = zero).show()
    plot_pacf(data, lags = lags, zero = zero).show()
    ax1.show()
