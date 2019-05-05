import pytest
import ie_group_1_mini_pandas as mini_pd


def test_sum():
    dictionary = {'col1': [1, 2], 'col2': [3, 4]}
    mdf = mini_pd.MiniDataFrame(dictionary)
    sum_mdf = mdf.sum
    assert sum_mdf[0] == 3  # col1: 1 + 2
    assert sum_mdf[1] == 7  # col2: 3 + 4
