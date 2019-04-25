"""
Mini_Pandas DataFrame
---------
Customized version of a DataFrame meant to mimic core functionalities of the Pandas DataFrame object.

"""

import numpy as np
import pandas as pd


class MiniDataFrame:

    @property
    def _constructor(self):
        return MiniDataFrame

    def __init__(self, data=None, index=None, columns=None, datatype=None):
        if data is None:
            data = {}
        
        if isinstance(data, dict):
            mgr = init_dict(data, index, columns, dtype=dtype)

    @property
    def get_row(self, index=None):
        """
        Return a list representing the corresponding values of the given row.
        Examples
        --------
        >>> df = minipd.MiniDataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.getrow(0)
        (1,2)
        """
        return list(self.columns[index])

    @property
    def sum(self):
        """
        Return a list of values corresponding to the sum of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.sum
        (3,7)
        """
        sum_output = [sum(self.columns[index]) if self.columns[index].datatype == 'a' for index in self.columns]
        return sum_output

    @property
    def median(self):
        """
        Return a list of values corresponding to the median of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.median
        
        """

        median_output = [median(self.columns[index]) if self.columns[index].datatype == 'a' for index in self.columns]
        return median_output

    @property
    def min(self):
        """
        Return a list of values corresponding to the min of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.min
        (1,3)

        """

        min_output = [min(self.columns[index]) if self.columns[index].datatype == 'a' for index in self.columns]
        return min_output

    @property
    def max(self):
        """
        Return a list of values corresponding to the max of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.max
        (2,4)

        """
        max_output = [max(self.columns[index]) if self.columns[index].datatype == 'a' for index in self.columns]
        return max_output
