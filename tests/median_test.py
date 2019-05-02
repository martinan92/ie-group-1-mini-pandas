import pytest
import ie_group_1_mini_pandas as mini_pd

def test_median():
    dictionary = {'col1': [1,2,3], 'col2': [4,5,6]}
    mdf = mini_pd.MiniDataFrame(dictionary)
    median_mdf = mdf.median
    assert median_mdf[0] == 2 
    assert median_mdf[1] == 5 