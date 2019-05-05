import pytest
import ie_group_1_mini_pandas as mini_pd


def test_get():
    dictionary = {'col1': [1, 2], 'col2': [3, 4]}
    mdf = mini_pd.MiniDataFrame(dictionary)
    col1 = mdf['col1']
    assert col1[0] == 1
    assert col1[1] == 2


def test_set():
    dictionary = {'col1': [1, 2], 'col2': [3, 4]}
    mdf = mini_pd.MiniDataFrame(dictionary)
    mdf['col1'] = [5, 6]
    col1 = mdf['col1']
    assert col1[0] == 5
    assert col1[1] == 6
