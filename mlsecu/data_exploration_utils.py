import pandas as pd

def get_column_names(dataframe):
    return dataframe.columns

def get_nb_of_dimensions(dataframe):
    return len(dataframe.columns)

def get_nb_of_rows(dataframe):
    if dataframe is None:
        return None
    return dataframe.shape[0]

def get_number_column_names(dataframe):
    if dataframe is None:
        return None
    object_columns = dataframe.select_dtypes(include=['int64', 'float64'])
    return object_columns.columns.tolist()

def get_object_column_names(dataframe):
    if dataframe is None:
        return None
    object_columns = dataframe.select_dtypes(include=['object'])
    return object_columns.columns.tolist()

def get_unique_values(dataframe, column_name):
    if dataframe is None:
        return None
    return dataframe[column_name].unique()

def get_nb_of_parameters(dataframe):
    if dataframe is None:
        return None
    return len(dataframe.columns)