from sklearn.impute import SimpleImputer
import numpy as np

def cleaning_missing_data(dataset, , strategy='median', missing_values=np.nan):
    imputer = SimpleImputer(missing_values= missing_values, 
    strategy=strategy)
    dados_imputados = imputer.fit_transform(dataset)
    return dados_imputados
