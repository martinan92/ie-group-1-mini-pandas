import pytest
import ie_group_1_mini_pandas as mini_pd

def test_get_row():
    dictionary = {'col1': [1,2], 'col2': [3,4]}
    mdf = mini_pd.MiniDataFrame(dictionary)
    row1 = mdf.get_row(1)
    assert row1[0] == 2
    assert row1[1] == 4
    