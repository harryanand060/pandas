# Pandas Methods

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
        
#### Data Frame Override Default Setting Option
    
* Setting maximum rows to be shown
        
        pd.options.display.max_rows = 10
  
* Setting minimum rows to be shown
        
        pd.set_option("display.min_rows", 5)
        
        OR
        
        pd.options.display.min_rows = 5

#### Read Dictionary 
  
Read dictionary into Data Frame, we can pass dict to the DataFrame

#### pd.DataFrame(dict)

* Method:
      
            pd.DataFrame(dict)
      
            dict_data = {"name": ["anand", "kumar"], "Roll": [1608060, 1608164]}
        
            data_frame = pd.DataFrame(dict_data)
  
* Output:
        
               name     Roll
            0  anand  1608060
            1  kumar  1608164
    
#### Read CSV, Excel Sheet 
  
Pandas DataFrame from CSV, read_csv('file_name') function that takes the file name as input and returns DataFrame as output

#### pd.read_csv(file_name.csv)

* Method:
      
            pd.read_csv("file_name.csv")
      
            data_frame = pd.read_csv("automobile_data.csv")
    
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

#### data_frame.info()

* Method:
    
        data_frame = pd.read_csv("automobile_data.csv")
      
        data_frame.info()
        
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

#### data_frame.describe()

* Method:
  
        data_frame = pd.read_csv("automobile_data.csv")
  
        data_frame.describe()

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

#### Data Frame Properties

We can get DataFrame properties/attributes using below method, like all index, all columns.

####data_frame.index

* Method:
    
      Return the Range of the row index
  
      data_frame.index
  
* Output:
  
      RangeIndex(start=0, stop=60, step=1) 

#### data_frame.columns

* Method: 

      Return a list of column labels
      
      data_frame.columns

* Output:

      Index(['company', 'body-style', 'length', 'engine-type', 'avg-mileage'],
    
#### data_frame.dtypes

* Method:

      Return column's data type

      data_frame.dtypes

* Output:

      company         object
      body-style      object
      length         float64
      engine-type     object
      avg-mileage      int64
      dtype: object 


#### Data Frame Selection

Data Frame Selection means we can select any particular rows, columns or rows in specific range.

#### data_frame.head(no_of_rows)

* Method:
    
      Return Top value from data frame 
      default 5 data frame

      data_frame.head()

* Output:

             company   body-style  length engine-type  avg-mileage
      0  alfa-romero  convertible   168.8        dohc           21
      1  alfa-romero    hatchback   171.2        ohcv           19
      2         audi        sedan   176.6         ohc           24
      3         audi        sedan   176.6         ohc           18
      4         audi        sedan   177.3         ohc           19

#### data_frame.tail(no_of_rows)

* Method:
      
      Return last value from data frame
      default 5 data frame
      
      data_frame.tail()

* Output:
  
             company body-style  length engine-type  avg-mileage
      55  volkswagen      sedan   171.7         ohc           27
      56  volkswagen      sedan   171.7         ohc           37
      57  volkswagen      sedan   171.7         ohc           26
      58       volvo      sedan   188.8         ohc           23
      59       volvo      wagon   188.8         ohc           23

#### data_frame.at[ row_index, column ]

* Method:
    
      Return selected row using index and column name
  
      data_frame.at[0, "company"]

* Output:
      
      alfa-romero


#### data_frame.iat[ row_index, column_index ]

* Method:

      Return slected row and column from data frame using index 
      
      data_frame.iat[0, 3]

* Output:

      dohc


#### data_frame.loc[ row_index_range, column_list ]

* Method:
  
      Return range of rows with multiple columns
      
      data_frame.loc[0:2,["company","body-style"]]

* Output:

           company   body-style
      0  alfa-romero  convertible
      1  alfa-romero    hatchback
      2         audi        sedan

#### data_frame.iloc[ rows_index_range, column_index_range ]

* Method:

      Return row and cloumn inbetween given range
  
      data_frame.iloc[0:2,0:3]

* Output:

             company   body-style  length
        0  alfa-romero  convertible   168.8
        1  alfa-romero    hatchback   171.2








