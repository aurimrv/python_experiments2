import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

# Test cases for fibonacci_dp function
def test_fibonacci_dp_zero():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_negative():
    assert fibonacci_dp(-5) == 0

def test_fibonacci_dp_small_number():
    assert fibonacci_dp(5) == 5

# Test cases for fibonacci_recursive function
def test_fibonacci_recursive_zero():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_negative():
    assert fibonacci_recursive(-5) == 0

def test_fibonacci_recursive_small_number():
    assert fibonacci_recursive(5) == 5