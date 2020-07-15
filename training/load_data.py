import pandas as pd
from sklearn.model_selection import train_test_split
def load_and_split_data(file_path, test_size=0.2, seed=22793):
    df = pd.read_excel(file_path)
    train_cols = list(df.columns)[:-2]
    test_cols = list(df.columns)[-2:]
    X = df[train_cols]
    Y1 = df[test_cols[0]]
    Y2 = df[test_cols[1]]
    X_train, X_test, Y1_train, Y1_test, Y2_train, Y2_test = train_test_split(X, Y1, Y2, test_size=test_size, random_state=seed)
    return X_train, X_test, Y1_train, Y1_test, Y2_train, Y2_test
