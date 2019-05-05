import pytest
import numpy as np
import ie_group_1_mini_pandas as mini_pd


def test_median():
    dictionary1 = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    mdf1 = mini_pd.MiniDataFrame(dictionary1)
    median_mdf1 = mdf1.median
    assert median_mdf1[0] == 2
    assert median_mdf1[1] == 5

    array1 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                                   columns=['a', 'b', 'c'])
    median_array1 = array1.median
    assert median_array1[0] == 4
    assert median_array1[1] == 5
    assert median_array1[2] == 6

    array2 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    median_array2 = array2.median
    assert median_array2[0] == 4
    assert median_array2[1] == 5
    assert median_array2[2] == 6
