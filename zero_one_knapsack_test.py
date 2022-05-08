#Tests for correctness of 0/1 knapsack implementations.
import pytest
from zero_one_knapsack_brute_force import brute_force
from zero_one_knapsack_dynamic_prog import dynamic_prog

@pytest.mark.parametrize(
    "capacity, weights, profits, expected",
    [
        (11, [3, 4, 5, 9, 4], [3, 4, 4, 10, 4], ([1, 1, 0, 0, 1], 11)),
        (14, [12, 2, 1, 1, 4], [4, 2, 1, 2, 10], ([0, 1, 1, 1, 1], 15)),
    ],
)
def test_bruteforce(capacity, weights, profits, expected):
    actual = brute_force(capacity, weights, profits)
    assert actual == expected

@pytest.mark.parametrize(
    "capacity, weights, profits, expected",
    [
        (11, [3, 4, 5, 9, 4], [3, 4, 4, 10, 4], ([1, 1, 0, 0, 1], 11)),
        (14, [12, 2, 1, 1, 4], [4, 2, 1, 2, 10], ([0, 1, 1, 1, 1], 15)),
    ],
)

def test_dynamic(capacity, weights, profits, expected):
    actual = dynamic_prog(capacity, weights, profits)
    assert actual == expected
    
