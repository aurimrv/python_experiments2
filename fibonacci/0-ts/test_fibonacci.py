import pytest
from fibonacci import fibonacci_dp, fibonacci_recursive

def test_fibonacci_dp():
    assert fibonacci_dp(-1) == 0
    assert fibonacci_dp(0) == 0
    assert fibonacci_dp(1) == 1
    assert fibonacci_dp(5) == 5
    assert fibonacci_dp(12) == 144

def test_fibonacci_recursive():
    assert fibonacci_recursive(-1) == 0
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(12) == 144

