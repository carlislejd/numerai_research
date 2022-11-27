from sklearn.preprocessing import OrdinalEncoder

def print_both(file, *args):
    toprint = ' '.join([str(arg) for arg in args])
    print(toprint)
    file.write(str(toprint) + "\n")

def categorical_encoded(df):
    """
    Encodes categorical data
    Args: Dataframe
    """
    categoricalcolumns = df.select_dtypes(include=["object"]).columns.tolist()
    print('Names of categorical columns : ', categoricalcolumns)
    encoder = OrdinalEncoder()
    for col in categoricalcolumns:
        df[col] = encoder.fit_transform(df[col].values.reshape(-1,1))
    return df