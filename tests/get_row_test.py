import pytest
import numpy as np
import ie_group_1_mini_pandas as mini_pd


def test_get_row():
    dictionary1 = {'col1': [1, 2], 'col2': [3, 4]}
    mdf1 = mini_pd.MiniDataFrame(dictionary1)
    mdf_row1 = mdf1.get_row(1)
    assert mdf_row1[0] == 2
    assert mdf_row1[1] == 4

    dictionary2 = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    mdf2 = mini_pd.MiniDataFrame(dictionary2)
    mdf_row2 = mdf2.get_row(1)
    assert mdf_row2[0] == 2
    assert mdf_row2[1] == 5

    dictionary3 = {'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]}
    mdf3 = mini_pd.MiniDataFrame(dictionary3)
    mdf_row3 = mdf3.get_row(1)
    assert mdf_row3[0] == 2
    assert mdf_row3[1] == 4
    assert mdf_row3[2] == 6

    array1 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                                   columns=['a', 'b', 'c'])
    array_row1 = array1.get_row(1)
    assert array_row1[0] == 4
    assert array_row1[1] == 5
    assert array_row1[2] == 6

    array2 = mini_pd.MiniDataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    array_row2 = array2.get_row(1)
    assert array_row2[0] == 4
    assert array_row2[1] == 5
    assert array_row2[2] == 6
