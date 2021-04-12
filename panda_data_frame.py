import pandas as pd

"""
pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
data: It takes input dict, list, set, ndarray, Iterable, or DataFrame. If the input is not provided, then it creates an empty DataFrame. The resultant column order follows the insertion order.
index: (Optional) It takes the list of row index for the DataFrame. The default value is a range of integers 0, 1,…n.
columns : (Optional) It takes the list of columns for the DataFrame. The default value is a range of integers 0, 1,…n.
dtype : (Optional) By default, It infers the data type from the data, but this option applies any specific data type to the whole DataFrame.
copy : (Optional) Copy data from inputs. Boolean, Default False. Only affects DataFrame or 2d array-like inputs
"""

# Setting maximum rows to be shown
pd.options.display.max_rows = 10
# Setting minimum rows to be shown
pd.set_option("display.min_rows", 5)
# OR
pd.options.display.min_rows = 5


def df_read_dict():
    """
    Pandas DataFrame from a dict object, we can pass it to the DataFrame
    constructor pd.DataFrame(dict)
    EX:
        name     Roll
    0  anand  1608060
    1  kumar  1608164

    :return: DataFrame
    """
    dict_data = {"name": ["anand", "kumar"], "Roll": [1608060, 1608164]}
    # student_dict = {'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}
    df_data = pd.DataFrame(dict_data)
    return df_data


def df_read_csv():
    """
    Pandas DataFrame from CSV, we use the read_csv('file_name') function that
    takes the file name as input and returns DataFrame as output
    EX:

            company   body-style  length engine-type  avg-mileage
    0   alfa-romero  convertible   168.8        dohc           21
    1   alfa-romero    hatchback   171.2        ohcv           19
    ..          ...          ...     ...         ...          ...
    58        volvo        sedan   188.8         ohc           23
    59        volvo        wagon   188.8         ohc           23

    [60 rows x 5 columns]

    :return: DataFrame
    """

    df_data = pd.read_csv("automobile_data.csv")
    return df_data


def df_meta_info(df_data):
    """
    DATA FRAME META DATA INFORMATION

    :param df_data: DataFrame

    EX:

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 60 entries, 0 to 59
    Data columns (total 5 columns):
     #   Column       Non-Null Count  Dtype
    ---  ------       --------------  -----
     0   company      60 non-null     object
     1   body-style   60 non-null     object
     2   length       60 non-null     float64
     3   engine-type  60 non-null     object
     4   avg-mileage  60 non-null     int64
    dtypes: float64(1), int64(1), object(3)
    memory usage: 2.5+ KB

    :return:
    """
    stats=df_data.info()
    out = f"METHOD: data_frame.describe\n\n"
    out += f"OUTPUT: \n{stats} \n\n"


def df_statistics(df_data):
    """
    mathematical statistics of the data in DataFrame

    :param df_data: DataFrame

    EX:
    METHOD: df_data.describe()
    OUTPUT:
               length  avg-mileage
    count   60.000000    60.000000
    mean   173.170000    25.883333
    std     14.128914     8.174146
    min    141.100000    13.000000
    25%    159.100000    19.000000
    50%    171.450000    25.000000
    75%    179.125000    31.000000
    max    208.100000    47.000000

    :return:
    """
    stats = df_data.describe()
    out = f"METHOD: data_frame.describe\n\n"
    out += f"OUTPUT: \n{stats} \n\n"
    return out


def fr_attributes(df_data):
    """

    :param df_data: Dataframe
    :return:
    """
    # output = f"Index: {data.index} \n Column: {data.columns}"
    key_dict = {"index": "gives the Range of the row index",
                "columns": "gives a list of column labels",
                "dtypes": "gives column names and their data type",
                "values": "gives all the rows in DataFrame",
                "empty": "used to check if the DataFrame is empty",
                "size": "gives a total number of values in DataFrame",
                "shape": "number of rows and columns in DataFrame"}
    out = ""
    for key, value in key_dict.items():
        item = getattr(df_data, key)
        out += f"{'*' * 20} Data Frame {key.upper()}: {value} {'*' * 20} \n"
        out += f"METHOD: data_frame.{key}\n\n"
        out += f"OUTPUT: {item} \n\n"
    return out


if __name__ == "__main__":
    data = df_read_csv()
    # print(data.to_json(orient='split'))
    print(df_statistics(data))
    # output.info()
    # print(output)
