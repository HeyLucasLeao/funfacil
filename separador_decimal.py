def separador_decimal_de_dataframe_inteiros(dataframe, column, inplace=False):
    df = dataframe.copy()
    df[column] = [int(x) for x in df[column]]
    df[column] = ["{:,}".format(x) for x in df[column]]
    df[column] = [x.replace(',','.') for x in df[column]]
    if inplace == True:
        dataframe[column] = df[column]
    return df
