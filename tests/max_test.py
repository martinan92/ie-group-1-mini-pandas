import pytest
import ie_group_1_mini_pandas as mini_pd

def test_max():
    dictionary = {'col1': [1,2], 'col2': [3,4]}
    mdf = mini_pd.MiniDataFrame(dictionary)
    max_mdf = mdf.max
    assert max_mdf[0] == 2
    assert max_mdf[1] == 4 