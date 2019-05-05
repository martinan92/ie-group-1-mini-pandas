import pytest
import numpy as np
import ie_group_1_mini_pandas as mini_pd


def test_sum():
    dictionary1 = {'col1': [1, 2], 'col2': [3, 4]}
    mdf1 = mini_pd.MiniDataFrame(dictionary1)
    sum_mdf1 = mdf1.sum
    assert sum_mdf1[0] == 3  # col1: 1 + 2
    assert sum_mdf1[1] == 7  # col2: 3 + 4

    dictionary2 = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    mdf2 = mini_pd.MiniDataFrame(dictionary2)
    sum_mdf2 = mdf2.sum
    assert sum_mdf2[0] == 6  # col1: 1 + 2 + 3
    assert sum_mdf2[1] == 15  # col2: 4 + 5 + 6

    dictionary3 = {'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]}
    mdf3 = mini_pd.MiniDataFrame(dictionary3)
    sum_mdf3 = mdf3.sum
    assert sum_mdf3[0] == 3  # col1: 1 + 2
    assert sum_mdf3[1] == 7  # col2: 3 + 4
    assert sum_mdf3[2] == 11  # col2: 5 + 6

    array1 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                                   columns=['a', 'b', 'c'])
    sum_array1 = array1.sum
    assert sum_array1[0] == 12  # col1: 1 + 4 + 7
    assert sum_array1[1] == 15  # col2: 2 + 5 + 8
    assert sum_array1[2] == 18  # col2: 3 + 6 + 9

    array2 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    sum_array2 = array2.sum
    assert sum_array2[0] == 12  # col1: 1 + 4 + 7
    assert sum_array2[1] == 15  # col2: 2 + 5 + 8
    assert sum_array2[2] == 18  # col2: 3 + 6 + 9
