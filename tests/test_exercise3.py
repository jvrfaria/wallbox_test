import pytest
from src.exercise3 import third_exercise


@pytest.mark.parametrize(
    "coinset, expected",
    [
        # TEST CASE 1: Number of coins is odd. More heads then tails. Input is str.
        ('01011011001', 3),
        # TEST CASE 2: Number of coins is odd. More tails then heads. Input is list.
        (['1', '1', '1', '0', '0', '0', '0', '0', '1'], 3),
        # TEST CASE 3: Number of coins is even. More tails at even positions than at odd positions. Input is tuple.
        (('0', '1', '1', '0'), 1),
        # TEST CASE 4: Number of coins is even. More tails at odd positions than at even positions. Input is str.
        ('111000', 1),
        # TEST CASE 5: Number of coins is even and input is already interspersed. Input is tuple.
        (('1', '0', '1', '0'), 0),
        # TEST CASE 6: Number of coins is odd and input is already interspersed. Input is list.
        (['0', '1', '0'], 0),
        # TEST CASE 7: Invalid input. Only one coin. Input is str
        ('0', None),
        # TEST CASE 8: Invalid input. There is an element different of '0' or '1'
        ('020', None)
    ]
)
def test_third_exercise(coinset, expected):
    assert third_exercise(coinset) == expected
