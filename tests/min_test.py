import pytest
import numpy as np
import ie_group_1_mini_pandas as mini_pd


def test_min():
    dictionary = {'col1': [1, 2], 'col2': [3, 4]}
    mdf1 = mini_pd.MiniDataFrame(dictionary)
    min_mdf1 = mdf1.min
    assert min_mdf1[0] == 1
    assert min_mdf1[1] == 3

    dictionary2 = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    mdf2 = mini_pd.MiniDataFrame(dictionary2)
    min_mdf2 = mdf2.min
    assert min_mdf2[0] == 1
    assert min_mdf2[1] == 4

    dictionary3 = {'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]}
    mdf3 = mini_pd.MiniDataFrame(dictionary3)
    min_mdf3 = mdf3.min
    assert min_mdf3[0] == 1
    assert min_mdf3[1] == 3
    assert min_mdf3[2] == 5

    array1 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                                   columns=['a', 'b', 'c'])
    min_array1 = array1.min
    assert min_array1[0] == 1
    assert min_array1[1] == 2
    assert min_array1[2] == 3

    array2 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    min_array2 = array2.min
    assert min_array2[0] == 1
    assert min_array2[1] == 2
    assert min_array2[2] == 3
