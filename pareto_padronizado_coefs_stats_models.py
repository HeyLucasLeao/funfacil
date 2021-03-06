def visualizar_modelo_treinado(model, alpha=0.05):
    from scipy import stats
    distribuicao = stats.t(df = model.df_resid)
    t_values = model.tvalues
    df = t_values.to_frame(name='coef').reset_index()
    df.rename(columns={'index': 'variaveis'}, inplace=True)
    limite = distribuicao.ppf(q= 1 - alpha/2)
    fig = px.bar(df.sort_values('coef', ascending=True), x='coef', y='variaveis')
    fig.add_vline(x= limite, line_color='red')
    return fig
