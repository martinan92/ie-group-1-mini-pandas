import pytest
import ie_group_1_mini_pandas as mini_pd


def test_shape():
    dictionary1 = {'col1': [1, 2], 'col2': [3, 4]}
    df1 = mini_pd.MiniDataFrame(dictionary1)
    assert df1.shape == (2, 2)

    dictionary2 = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    df2 = mini_pd.MiniDataFrame(dictionary2)
    assert df2.shape == (3, 2)

    dictionary2 = {'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]}
    df2 = mini_pd.MiniDataFrame(dictionary2)
    assert df2.shape == (2, 3)
