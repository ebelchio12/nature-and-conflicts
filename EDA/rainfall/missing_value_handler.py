import pandas as pd
import numpy as np

def add_missing_years(df: pd.DataFrame, min_year=1960, max_year=2023, year_name='Year', ref_column='Code') -> pd.DataFrame:
    '''
    In a dataframe with yearly data, add rows with missing years (given a range of years),
    within a certain value for a reference column.

    Allows for adding rows for missing years for each country.

    Inputs:
    - df -> DataFrame to be modified
    - min_year -> year (int, default 1960)
    - max_year -> year (int, default 2023)
    - year_name -> name of the year column (str, default 'Year')
    - ref_column -> name of the column to group by (str, 'Code')

    Output:
    - pandas DataFrame
    '''
    cats = df[ref_column].unique()
    for cat in cats:
        for year in range(min_year, max_year + 1):
            if len( df[ (df[ref_column]==cat) & (df[year_name]==year) ] ) == 0:
                # TODO: this is horrible and slow af
                new_row = {year_name: year, ref_column: cat}
                df = pd.concat([df, pd.DataFrame([new_row])])

    return df

def fill_na(df: pd.DataFrame, column_name: str, ref_col: str, ref_val: str, method='mode', value=None) -> pd.DataFrame:
    '''
    Function to replace na's in rows for a given column using a specific rule.

    Inputs:
    - df -> DataFrame to be modified
    - column_name -> name of the column to be filled
    - ref_col -> reference column name to group by
    - ref_val -> value of reference column to group by
    - method ('mode', 'min', 'max', 'mean', 'value') -> the method to use to fill 
    - value -> value to fill by (if method='value')

    Output:
    - df -> modified dataframe
    '''
    if method not in ['mode', 'min', 'max', 'mean', 'value']:
        raise ValueError(f"{method} not valid")
    if method == 'value' and value is None:
        raise ValueError(f"Method is set to value but value is None.")
    
    col_type = df[column_name].dtype
    if method in ['min', 'max', 'mean'] and not np.issubdtype(col_type, np.number):
        raise TypeError(f"Method {method} is not compatible with column type {col_type}.")
    if method == 'value' and (col_type != type(value)):
        raise TypeError(f"Given value type {type(value)} is not compatible with column type {col_type}.")

    if method == 'mode':
        fill_value = df[df[ref_col]==ref_val][column_name].mode()[0]
    elif method == 'min':
        fill_value = df[df[ref_col]==ref_val][column_name].min()
    elif method == 'max':
        fill_value = df[df[ref_col]==ref_val][column_name].max()
    elif method == 'mean':
        fill_value = df[df[ref_col]==ref_val][column_name].mean()
    else:
        fill_value = value

    df.loc[(df[ref_col] == ref_val) & (df[column_name].isna()), column_name] = fill_value