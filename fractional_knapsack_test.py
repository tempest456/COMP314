#Tests for correctness of fractional knapsack implementations.
import pytest
from fractional_knapsack_brute_force import brute_force 
from fractional_knapsack_greedy import greedy

@pytest.mark.parametrize(
    "capacity, weights, profits, expected",
    [
        (60, [40, 10, 20, 24], [280, 100, 120, 120], ([1, 1, 0.5, 0], 440.0)),
        (15, [2, 3, 5, 7, 1, 4, 1], [10, 5, 15, 7, 6, 18, 3], ([1, 0.67, 1, 0, 1, 1, 1], 55.33)),
    ],
)
def test_greedy(capacity, weights, profits, expected):
    actual = greedy(capacity, weights, profits)
    assert pytest.approx(actual, rel=1e-2) == expected

@pytest.mark.parametrize(
    "capacity, weights, profits, expected",
        [
        (60, [40, 10, 20, 24], [280, 100, 120, 120], ([1, 0, 1, 0], 400)),
        (15, [2, 3, 5, 7, 1, 4, 1], [10, 5, 15, 7, 6, 18, 3], ([1, 1, 1, 0, 1, 1, 0], 54)),
        ],
)
def test_bruteforce(capacity, weights, profits, expected):
    actual = brute_force(capacity, weights, profits)
    assert pytest.approx(actual, rel=1e-2) == expected
    
