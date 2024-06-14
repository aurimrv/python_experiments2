import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import fibonacci

def test_fibonacci_dp():
    assert fibonacci.fibonacci_dp(0) == 0
    assert fibonacci.fibonacci_dp(1) == 1
    assert fibonacci.fibonacci_dp(5) == 5
    assert fibonacci.fibonacci_dp(10) == 55

def test_fibonacci_recursive():
    assert fibonacci.fibonacci_recursive(0) == 0
    assert fibonacci.fibonacci_recursive(1) == 1
    assert fibonacci.fibonacci_recursive(5) == 5
    assert fibonacci.fibonacci_recursive(10) == 55