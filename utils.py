import pandas as pd
import numpy as np
import chardet
import io

def load_data(file):
    file_name = file.name
    if file_name.endswith('.csv'):
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        file.seek(0)
        return pd.read_csv(io.BytesIO(raw_data), encoding=encoding)
    elif file_name.endswith(('.xlsx', '.xls')):
        return pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format")

def get_data_summary(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "types": df.dtypes.to_dict(),
        "missing": df.isnull().sum().to_dict(),
        "missing_pct": (df.isnull().sum() / len(df) * 100).to_dict()
    }

def get_descriptive_stats(df):
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty: return None
    desc = numeric_df.describe().T
    desc['median'] = numeric_df.median()
    return desc

def get_correlation_matrix(df):
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.shape[1] < 2: return None
    return numeric_df.corr(method='spearman')
