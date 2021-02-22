from sklearn.impute import SimpleImputer
import numpy as np

def cleaning_missing_data(data_frame, , strategy='median', missing_values=np.nan):
    imputer = SimpleImputer(missing_values= missing_values, 
    strategy=strategy)
    dados_imputados = imputer.fit_transform(data_frame)
    return dados_imputados
