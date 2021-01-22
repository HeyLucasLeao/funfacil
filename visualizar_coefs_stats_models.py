def visualizar_modelo_ajustado(model, alpha=0.5, x=None, y=None):
    from scipy import stats
    distribuicao = stats.t(df = model.df_resid)
    t_values = model.tvalues
    df = t_values.to_frame(name='coef').reset_index()
    df.rename(columns={'index': 'variaveis'}, inplace=True)
    limite = distribuicao.ppf(q= 1 - (alpha/2))*len(df)
    fig = px.bar(df.sort_values('coef', ascending=True), x=x, y=y)
    fig.add_vline(x= limite, line_color='red')
    return fig
