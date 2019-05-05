import pytest
import numpy as np
import ie_group_1_mini_pandas as mini_pd

@pytest.mark.parametrize('dic_array, cols, expected_result', 
    [
        ({'col1': [2, 4], 'col2': [4, 8]}, None, [6, 12]),
        ({'col1': [1, 2, 3], 'col2': [4, 5, 6]}, None, [6, 15]),
        ({'col1': [2, 4], 'col2': [6, 8], 'col3': [10, 12]}, None, [6, 14, 22]),
        (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), ['a', 'b', 'c'], [12, 15, 18]),
        (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), None, [12, 15, 18])
    ]
)

def test_sum(dic_array, cols, expected_result):
    df = mini_pd.MiniDataFrame(dic_array, columns=cols)
    sum_df = df.sum
    assert all([a == b for a, b in zip(df.sum, expected_result)])