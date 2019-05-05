import pytest
import numpy as np
import ie_group_1_mini_pandas as mini_pd


@pytest.mark.parametrize('dic_array, cols, expected_result',
                         [
                            ({'col1': [1, 2], 'col2': [3, 4]},
                             None, [2, 4]),
                            ({'col1': [1, 2, 3], 'col2': [4, 5, 6]},
                             None, [3, 6]),
                            ({'col1': [1, 2], 'col2': [3, 4],
                             'col3': [5, 6]}, None, [2, 4, 6]),
                            (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                             ['a', 'b', 'c'], [7, 8, 9]),
                            (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                             None, [7, 8, 9])
                         ]
                         )
def test_max(dic_array, cols, expected_result):
    df = mini_pd.MiniDataFrame(dic_array, columns=cols)
    max_df = df.max
    assert all([a == b for a, b in zip(df.max, expected_result)])
