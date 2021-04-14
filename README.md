# Pandas Practice

###Install Pandas
    
    pip install pandas

### Data Frame
    
####Function
  
    pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

#### Parameter    
    
    **data**: It takes input dict, list, set, ndarray, Iterable, or DataFrame. 
    If the input is not provided, then it creates an empty DataFrame. 
    The resultant column order follows the insertion order.

    **index**: (Optional) It takes the list of row index for the DataFrame. 
    The default value is a range of integers 0, 1,…n.

    **columns** : (Optional) It takes the list of columns for the DataFrame. 
    The default value is a range of integers 0, 1,…n.

    **dtype** : (Optional) By default, It infers the data type from the data,
    but this option applies any specific data type to the whole DataFrame.

    **copy** : (Optional) Copy data from inputs. Boolean, Default False. 
    Only affects DataFrame or 2d array-like inputs
    

