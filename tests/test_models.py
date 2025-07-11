"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean,  daily_max, daily_min

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""


    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_handle_Nans():
    """Test that mean function works for an array of zeros."""


    test_input = np.array([[ np.nan, -100, 2],
                           [1,  0,  np.inf],
                           [3,  0,  42]])
    test_result = np.array([3, 100, np.inf ])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input, abs=True), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_min_string():
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])


# This decorator "parameterize" repeatedly runs the function following it
# with the corresponding input variables from the tuple you give it.
@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


@pytest.mark.parametrize("a,b,result", [(1, 2, 3), (2, 3, 5)])
def test_add(a, b, result):
    assert a + b == result