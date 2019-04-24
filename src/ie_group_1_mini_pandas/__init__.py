"""
Mini_Pandas DataFrame
---------
Customized version of a DataFrame meant to mimic core functionalities of the Pandas DataFrame object.

"""

import numpy as np
import pandas as pd

class MiniDataFrame:
    def __init__(self, data = None, index = None, columns = None, datatype = None): 
        if data is None:
            data = {}
    
    @property
    def get_row(self):
        """
        Return a list representing the corresponding values of the given row.
        Examples
        --------
        >>> df = minipd.MiniDataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.getrow

        """

    @property
    def sum(self):
         """
        Return a list of values corresponding to the sum of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.sum

        """

    @property
    def median(self):
        """
        Return a list of values corresponding to the median of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.median

        """

    @property
    def min(self):
        """
        Return a list of values corresponding to the min of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.min

        """
    
    @property
    def max(self):
        """
        Return a list of values corresponding to the max of each numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.max

        """
