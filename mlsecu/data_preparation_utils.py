import pandas as pd

def get_one_hot_encoded_dataframe(dataframe):
    if dataframe is None:
        return None
    return pd.get_dummies(dataframe)

def remove_nan_through_mean_imputation(dataframe):
    if dataframe is None:
        return None
    return dataframe.fillna(dataframe.mean(numeric_only=True))
