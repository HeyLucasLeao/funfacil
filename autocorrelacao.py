def autocorrelacao(data, title='Correlação de Dados', figsize=(12,6)):
    from pandas.plotting import autocorrelation_plot
    import matplotlib.pyplot as plt    
    ax = plt.figure(figsize=figsize)
    ax.suptitle(title, fontsize=18, x= 0.26, y= 0.95)
    autocorrelation_plot(data)
    return ax
