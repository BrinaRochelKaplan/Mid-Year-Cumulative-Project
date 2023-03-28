import pandas as pd
def convert_to_bool(col):
    col = col.astype(bool)

def convert_to_datetime(col):
    col = pd.to_datetime(col)

def creating_date_column(df, col_lst, new_col):
    df[new_col] = df[col_lst].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
    # converting 'arrival_date' column to datetime object
    df[new_col] = pd.to_datetime(df[new_col], format='%Y_%B_%d')
# dropping the cols
def drop_col(df, cols):
    df.drop(columns=cols, inplace=True)

def new_col_from_other_cols(df, new_col, col1, col2):
    df[new_col] = df.apply(lambda row:False if row[col1] > 0 else(False if  row[col2] > 0 else True),axis=1)

def replace_nan(col, value=None, method = None):
    col.fillna(value, method, inplace=True)
