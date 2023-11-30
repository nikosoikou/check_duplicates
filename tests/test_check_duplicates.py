import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from src.duplicates import check_duplicates


@pytest.fixture
def df():
    return pd.DataFrame(
        data=[
            ['A', 'a', 'x', 1],
            ['A', 'b', 'x', 1],
            ['A', 'c', 'x', 1],
            ['B', 'a', 'x', 1],
            ['B', 'b', 'x', 1],
            ['B', 'c', 'x', 1],
            ['A', 'a', 'y', 1],
        ],
        columns=['col_1', 'col_2', 'col_3', 'col_4']
    )


def test_check_duplicates_col_1(df):
    expected_output = {
        'count': 7,
        'samples': pd.DataFrame({
            'col_1': ['A', 'B'],
            'number_of_duplicates': [4, 3]
        })
    }
    actual_output = check_duplicates(df, ['col_1'])

    assert actual_output['count'] == expected_output['count']
    assert_frame_equal(actual_output['samples'], expected_output['samples'])


def test_check_duplicates_col_1_col_2(df):
    expected_output = {
        'count': 2,
        'samples': pd.DataFrame({
            'col_1': ['A'],
            'col_2': ['a'],
            'number_of_duplicates': [2]
        })
    }
    actual_output = check_duplicates(df, ['col_1', 'col_2'])

    assert actual_output['count'] == expected_output['count']
    assert_frame_equal(actual_output['samples'], expected_output['samples'])


def test_check_duplicates_col_1_col_2_col_3(df):
    output = check_duplicates(df, ['col_1', 'col_2', 'col_3'])

    assert output['count'] == 0
    assert output['samples'].empty


def test_check_duplicates_col_1_col_2_col_3_col_4(df):
    output = check_duplicates(df, ['col_1', 'col_2', 'col_3', 'col_4'])

    assert output['count'] == 0
    assert output['samples'].empty


def test_check_duplicates_exception(df):
    invalid_input = False

    # Call the function with invalid input
    with pytest.raises(KeyError):
        check_duplicates(df, invalid_input)
