def dados_apresentaveis(x):
    x = round(x)
    x ="{:,}".format(x)
    x = x.replace(',','.')
    return x
