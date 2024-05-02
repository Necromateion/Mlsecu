import pandas as pd
import sklearn
import mlsecu.data_exploration_utils as da
import mlsecu.data_preparation_utils as dp


def get_list_of_attack_types(dataframe):
    if dataframe is None:
        return None
    return dataframe['attack_type'].unique().tolist()

def get_nb_of_attack_types(dataframe):
    if dataframe is None:
        return None
    return len(dataframe['attack_type'].unique())

from sklearn.ensemble import IsolationForest

def remove_nan_through_mean_imputation(dataframe):
    if dataframe is None:
        return None
    return dataframe.fillna(dataframe.mean(numeric_only=True))

def get_list_of_if_outliers(dataframe, outlier_fraction):    
    columns_selected = ['src_port', 'dest_port', 'pkt_size', 'timestep']    
    dataframe[columns_selected] = remove_nan_through_mean_imputation(dataframe[columns_selected])
    dataframe = pd.get_dummies(dataframe)
    model = IsolationForest(contamination=outlier_fraction, random_state=42)
    model.fit(dataframe)
    outlier_labels = model.predict(dataframe)
    outlier_indices = dataframe[outlier_labels == -1].index.tolist()
    return outlier_indices



from sklearn.neighbors import LocalOutlierFactor

def get_list_of_lof_outliers_df(dataframe, outlier_fraction):
    columns_selected = ['src_port', 'dest_port', 'pkt_size', 'timestep']    
    dataframe[columns_selected] = remove_nan_through_mean_imputation(dataframe[columns_selected])
    dataframe = pd.get_dummies(dataframe)

    lof_model = LocalOutlierFactor(contamination=outlier_fraction)
    
    preds = lof_model.fit_predict(dataframe)
    
    outliers = dataframe[preds == -1]
    
    return outliers

def get_list_of_lof_outliers(dataframe, outlier_fraction):
    df = get_list_of_lof_outliers_df(dataframe, outlier_fraction)
    return df.index.tolist()

def get_list_of_parameters(dataframe):
    if dataframe is None:
        return None
    return dataframe.columns.tolist()

def get_nb_of_if_outliers(dataframe, outlier_fraction):
    outliers = get_list_of_if_outliers_df(dataframe, outlier_fraction)
    return len(outliers)

def get_nb_of_lof_outliers(dataframe, outlier_fraction):
    outliers = get_list_of_lof_outliers_df(dataframe, outlier_fraction)
    return len(outliers)

def get_nb_of_occurrences(dataframe):
    if dataframe is None:
        return None
    return dataframe.shape[0]

def get_nb_of_parameters(dataframe):
    if dataframe is None:
        return None
    return len(dataframe.columns)
