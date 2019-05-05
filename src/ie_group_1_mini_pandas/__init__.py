"""
Mini_Pandas DataFrame
---------
Customized version of a DataFrame meant to mimic core functionalities
of the Pandas DataFrame object.

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
        else:
            self.datatype = datatype

        if index is None:
            self.index = list(range(0, len(data), 1))

        # Check type of data structure entered
        if isinstance(data, dict):
            self.columns = list(data.keys())
            names = list(data.keys())
            data_array = np.transpose([value for index, value in data.items()])

            all_elements = []
            for key in data:
                row_elements = []
                for value in data[key]:
                    row_elements.append(type(value))
                all_elements.append(row_elements[0])

            formats = list(all_elements)
            dtype = dict(names=names, formats=formats)
            data_array = [tuple(item) for item in data_array]
            self.data = np.array(data_array, dtype=dtype)

        else:
            if columns is None:
                self.columns = list(range(0, len(data[0]), 1))
                self.data = np.transpose(data)
            else:
                all_elements = []
                for item in data:
                    row_elements = []
                    for element in item:
                        row_elements.append(type(element))
                    all_elements.append(row_elements[0])

                self.columns = columns
                formats = list(all_elements)
                dtype = dict(names=self.columns, formats=formats)
                data_array = [tuple(item) for item in data]
                self.data = np.array(data_array, dtype=dtype)

    def __iter__(self):
        return self.data.items()

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, item):
        self.data[index] = item

    def __len__(self):
        return len(self.__dict__)

    def get_row(self, index=None):
        """
        Return a list representing the corresponding values of the given row.
        Examples
        --------
        >>> df = mini_pd.MiniDataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.getrow(0)
        (1,3)
        """
        return self.data[index]

    @property
    def shape(self):
        """
        Return a tuple representing the dimensionality of the DataFrame.
        See Also
        --------
        ndarray.shape
        Examples
        --------
        >>> df = mini_pd.MiniDataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.shape
        (2, 2)
        """
        return len(self[self.columns[0]]), len(self.columns)

    @property
    def sum(self):
        """
        Return a list of values corresponding to the sum of each numerical
        column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = mini_pd.MiniDataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.sum
        (3,5)

        """
        _NUMERIC_KINDS = set('buifc')
        sum_output = [sum(self[cols]) for cols in self.columns
                      if self[cols].dtype.kind in _NUMERIC_KINDS]
        return(sum_output)

    @property
    def median(self):
        """
        Return a list of values corresponding to the median of each
        numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = mini_pd.MiniDataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.median

        """
        _NUMERIC_KINDS = set('buifc')
        median_output = [np.median(self[cols]) for cols in self.columns
                         if self[cols].dtype.kind in _NUMERIC_KINDS]
        return(median_output)

    @property
    def min(self):
        """
        Return a list of values corresponding to the min of each
        numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = mini_pd.MiniDataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.min
        (1,3)

        """
        _NUMERIC_KINDS = set('buifc')
        min_output = [np.min(self[cols]) for cols in self.columns
                      if self[cols].dtype.kind in _NUMERIC_KINDS]
        return min_output

    @property
    def max(self):
        """
        Return a list of values corresponding to the min of each
        numerical column while ignoring non-numerical columns.
        Examples
        --------
        >>> df = mini_pd.MiniDataFrame({'col1': [1, 2], 'col2': [3, 4]})
        >>> df.min
        (2,4)

        """
        _NUMERIC_KINDS = set('buifc')
        max_output = [np.max(self[cols]) for cols in self.columns
                      if self[cols].dtype.kind in _NUMERIC_KINDS]
        return max_output
