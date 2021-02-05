def seasonal_decompose(data, model, figsize=(15,8), period=None):
    from statsmodels.tsa.seasonal import seasonal_decompose
    import matplotlib.pyplot as plt 
    
    s_dec = seasonal_decompose(data, model = model, period=period)
    fig, (ax0, ax1,ax2,ax3) = plt.subplots(4,1, figsize=figsize)
    s_dec.observed.plot(ax=ax0, grid=True, legend=True)
    s_dec.trend.plot(ax=ax1, grid=True, legend=True)
    s_dec.seasonal.plot(ax=ax2, grid=True, legend=True)
    s_dec.resid.plot(ax=ax3, grid=True, legend=True)
