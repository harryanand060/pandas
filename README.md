# Pandas Practice

### Install 
    
    pip install pandas

### CSV FILE

    automobile_data.csv

* Note: Attached in the repo
    
### Data Frame

* Function
  
        pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

* Parameters    
    
        data: It takes input dict, list, set, ndarray, Iterable, or DataFrame. 
        If the input is not provided, then it creates an empty DataFrame. 
        The resultant column order follows the insertion order.
    
        index: (Optional) It takes the list of row index for the DataFrame. 
        The default value is a range of integers 0, 1,…n.
    
        columns : (Optional) It takes the list of columns for the DataFrame. 
        The default value is a range of integers 0, 1,…n.
    
        dtype : (Optional) By default, It infers the data type from the data,
        but this option applies any specific data type to the whole DataFrame.
    
        copy : (Optional) Copy data from inputs. Boolean, Default False. 
        Only affects DataFrame or 2d array-like inputs
        
#### Data Frame Overide Default Setting Option
    
* Setting maximum rows to be shown
        
        pd.options.display.max_rows = 10
  
* Setting minimum rows to be shown
        
        pd.set_option("display.min_rows", 5)
        
        OR
        
        pd.options.display.min_rows = 5

#### Read Dictionary 
  
Read dictionary into Data Frame, we can pass it to the DataFrame 
* Method:
      
            pd.DataFrame(dict)
      
            dict_data = {"name": ["anand", "kumar"], "Roll": [1608060, 1608164]}
        
            df_data = pd.DataFrame(dict_data)
  
* Output:
        
               name     Roll
            0  anand  1608060
            1  kumar  1608164
    
#### Read CSV, Excel Sheet 
  
Pandas DataFrame from CSV, we use the read_csv('file_name') function that takes the file name as input and returns DataFrame as output

* Method:
      
            pd.read_csv("file_name.csv")
      
            df_data = pd.read_csv("automobile_data.csv")
    
* Output:
    
                     company   body-style  length engine-type  avg-mileage
            0   alfa-romero  convertible   168.8        dohc           21
            1   alfa-romero    hatchback   171.2        ohcv           19
            ..          ...          ...     ...         ...          ...
            58        volvo        sedan   188.8         ohc           23
            59        volvo        wagon   188.8         ohc           23
        
            [60 rows x 5 columns]
    
#### Data Frame Meta Information
Data frame meta information like total rows, total column, data types of column.

* Method:
  
        df_data.info()
        
*Output:
        
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

#### Data Frame Statistics 

Mathematical statistics of the data in DataFrame Like Mean, Min, Max data value

* Method:
        
        df_data.describe()

* Output:

                length      avg-mileage
        count   60.000000    60.000000
        mean   173.170000    25.883333
        std     14.128914     8.174146
        min    141.100000    13.000000
        25%    159.100000    19.000000
        50%    171.450000    25.000000
        75%    179.125000    31.000000
        max    208.100000    47.000000