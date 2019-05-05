import pytest
import ie_group_1_mini_pandas as mini_pd

def test_shape():
    dictionary = {'col1': [1, 2], 'col2': [3, 4]}
    df = mini_pd.MiniDataFrame(dictionary)
    assert df.shape == (2,2)