import pytest
import numpy as np
import ie_group_1_mini_pandas as mini_pd


def test_max():
    dictionary = {'col1': [1, 2], 'col2': [3, 4]}
    mdf1 = mini_pd.MiniDataFrame(dictionary)
    max_mdf1 = mdf1.max
    assert max_mdf1[0] == 2
    assert max_mdf1[1] == 4

    dictionary2 = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    mdf2 = mini_pd.MiniDataFrame(dictionary2)
    max_mdf2 = mdf2.max
    assert max_mdf2[0] == 3
    assert max_mdf2[1] == 6

    dictionary3 = {'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]}
    mdf3 = mini_pd.MiniDataFrame(dictionary3)
    max_mdf3 = mdf3.max
    assert max_mdf3[0] == 2
    assert max_mdf3[1] == 4
    assert max_mdf3[2] == 6

    array1 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                                   columns=['a', 'b', 'c'])
    max_array1 = array1.max
    assert max_array1[0] == 7
    assert max_array1[1] == 8
    assert max_array1[2] == 9

    array2 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    max_array2 = array2.max
    assert max_array2[0] == 7
    assert max_array2[1] == 8
    assert max_array2[2] == 9
