import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

# Test cases for fibonacci_dp
def test_fibonacci_dp_with_0():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_with_1():
    assert fibonacci_dp(1) == 1

def test_fibonacci_dp_with_5():
    assert fibonacci_dp(5) == 5

def test_fibonacci_dp_with_negative():
    assert fibonacci_dp(-5) == 0

def test_fibonacci_dp_with_large_value():
    assert fibonacci_dp(10) == 55

# Test cases for fibonacci_recursive
def test_fibonacci_recursive_with_0():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_with_1():
    assert fibonacci_recursive(1) == 1

def test_fibonacci_recursive_with_5():
    assert fibonacci_recursive(5) == 5

def test_fibonacci_recursive_with_negative():
    assert fibonacci_recursive(-5) == 0

def test_fibonacci_recursive_with_large_value():
    assert fibonacci_recursive(10) == 55