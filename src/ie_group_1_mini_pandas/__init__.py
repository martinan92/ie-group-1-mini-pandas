"""
Mini_Pandas DataFrame
---------
Customized version of a DataFrame meant to mimic core functionalities of the Pandas DataFrame object.

"""

import numpy as np

class MiniDataFrame:

    @property
    def _constructor(self):
        return MiniDataFrame

    def __init__(self, data=None, index=None, columns=None, datatype=None):
        if data is None:
            data = {}
        if datatype is not None:
            datatype = self._validate_dtype(datatype)
        
        self.datatype = datatype
        
        if index is None:
            self.index = list(range(0, len(data), 1))
        
        # Check type of data structure entered
        if isinstance(data, dict):             
            data_array = []
            for index, value in data.items():
                data_array.append(value)
                
            self.data = np.transpose(data_array)
            self.columns = list(data.keys())      
        else:
            self.data = np.transpose(data)
            if columns is None:
                self.columns = list(data.keys()) 
            else:
                self.columns = columns

    @property
    def get_row(self, index=None):
        """
        Return a list representing the corresponding values of the given row.
        Examples
        --------
        >>> df = minipd.MiniDataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.getrow(0)
        (1,3)
        """

        row = [col[index] for col in self.columns]
        return row
            
    @property
    def sum(self):
        """
        Return a list of values corresponding to the sum of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = minipd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.sum
        (3,7)
        """
        _NUMERIC_KINDS = set('buifc')
        sum_output = [sum(self[:,cols]) for cols in self.columns if np.asarray(self[cols]).dtype.kind in _NUMERIC_KINDS]
        
        return(sum_output)
    
    
    @property
    def median(self):
        """
        Return a list of values corresponding to the median of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = minipd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.median
        
        """
        _NUMERIC_KINDS = set('buifc')     
        median_output = [np.median(self[:,cols]) for cols in self.columns if np.asarray(self[cols]).dtype.kind in _NUMERIC_KINDS]

        return(median_output)
    
    @property
    def min(self):
        """
        Return a list of values corresponding to the min of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = minipd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.min
        (1,3)

        """
        _NUMERIC_KINDS = set('buifc')     
        min_output = [np.min(self[:,cols]) for cols in self.columns if np.asarray(self[cols]).dtype.kind in _NUMERIC_KINDS]

        return min_output
    
    @property
    def max(self):
        """
        Return a list of values corresponding to the min of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = minipd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.min
        (2,4)

        """
        _NUMERIC_KINDS = set('buifc')     
        max_output = [np.max(self[:,cols]) for cols in self.columns if np.asarray(self[cols]).dtype.kind in _NUMERIC_KINDS]
        
        return max_output
    
