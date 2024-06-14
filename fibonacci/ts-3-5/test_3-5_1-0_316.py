import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

import pytest
import fibonacci

def test_fibonacci_dp_zero():
    assert fibonacci.fibonacci_dp(0) == 0

def test_fibonacci_dp_one():
    assert fibonacci.fibonacci_dp(1) == 1

def test_fibonacci_dp_positive():
    assert fibonacci.fibonacci_dp(5) == 5

def test_fibonacci_dp_negative():
    assert fibonacci.fibonacci_dp(-5) == 0

def test_fibonacci_recursive_zero():
    assert fibonacci.fibonacci_recursive(0) == 0

def test_fibonacci_recursive_one():
    assert fibonacci.fibonacci_recursive(1) == 1

def test_fibonacci_recursive_positive():
    assert fibonacci.fibonacci_recursive(6) == 8

def test_fibonacci_recursive_negative():
    assert fibonacci.fibonacci_recursive(-6) == 0