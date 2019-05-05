import pytest
import numpy as np
import ie_group_1_mini_pandas as mini_pd


@pytest.mark.parametrize('dic, expected_result', 
    [
        ({'col1': [1, 2], 'col2': [3, 4]}, (2, 2)),
        ({'col1': [1, 2, 3], 'col2': [4, 5, 6]}, (3, 2)),
        ({'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]}, (2, 3)),
        (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
         columns=['a', 'b', 'c'], (3, 3)),
        (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (3, 3))
    ]
)

def test_shape(dic, expected_result):
    dictionary = dic
    df = mini_pd.MiniDataFrame(dictionary)
    assert df.shape == expected_result


