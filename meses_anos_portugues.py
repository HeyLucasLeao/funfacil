from calendar import month_abbr
from datetime import datetime
import numpy as np

def meses_anos(data):
    
    dici = {'Jan': 'Jan',
            'Feb': 'Fev',
            'Mar': 'Mar',
            'Apr': 'Abr', 
            'May': 'Maio',
        'Jun': 'Jun',
        'Jul': 'Jul',
        'Aug': 'Ago',
        'Sep': 'Set',
        'Oct': 'Out', 
        'Nov': 'Nov',
        'Dec': 'Dez'}
    dois_meses_seguintes = str(datetime.now() + timedelta(weeks=8))[:10]
    
    dias = np.arange(data, dois_meses_seguintes, dtype='datetime64[M]')
    anos_sigla = [str(x)[:4] for x in dias]
    mes_int = [int(str(x)[5:7]) for x in dias]
    mes_sigla_ingles = [month_abbr[x] for x in mes_int]
    mes_sigla_portugues = [dici[x] for x in mes_sigla_ingles]
    
    meses_anos = [" ".join((x, y)) for x,y in zip(mes_sigla_portugues, anos_sigla)]

    return meses_anos
    
