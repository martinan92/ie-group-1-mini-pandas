import pytest
import ie_group_1_mini_pandas as mini_pd

def test_len():
    dictionary = {'col1': [1,2], 'col2': [3,4]}
    mdf = mini_pd.MiniDataFrame(dictionary)
    assert len(mdf) == 4
    assert len(mdf[1]) == 2