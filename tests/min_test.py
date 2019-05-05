import pytest
import ie_group_1_mini_pandas as mini_pd


def test_min():
    dictionary = {'col1': [1, 2], 'col2': [3, 4]}
    mdf = mini_pd.MiniDataFrame(dictionary)
    min_mdf = mdf.min
    assert min_mdf[0] == 1
    assert min_mdf[1] == 3
