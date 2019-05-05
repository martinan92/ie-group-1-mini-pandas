import pytest
import numpy as np
import ie_group_1_mini_pandas as mini_pd


@pytest.mark.parametrize('dic_array, cols, expected_result', 
    [
        ({'col1': [2, 4], 'col2': [4, 8]}, None, [3, 6]),
        ({'col1': [1, 2, 3], 'col2': [4, 5, 6]}, None, [2, 5]),
        ({'col1': [2, 4], 'col2': [6, 8], 'col3': [10, 12]}, None, [3, 7, 11]),
        (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), ['a', 'b', 'c'], [4, 5, 6]),
        (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), None, [4, 5, 6])
    ]
)

def test_median(dic_array, cols, expected_result):
    df = mini_pd.MiniDataFrame(dic_array, columns=cols)
    median_df = df.median
    assert all([a == b for a, b in zip(df.median, expected_result)])