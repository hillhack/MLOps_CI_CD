import pandas as pd

def load_data(path="data/iris_data.csv"):
    return pd.read_csv(path)

def validate_data(df):
    assert not df.empty, "Dataset is empty"
    assert df.isnull().sum().sum() == 0, "Missing values present"
    return True
