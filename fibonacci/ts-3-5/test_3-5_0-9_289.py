import os
import sys

# Import modules from the correct directory
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

# Test cases for fibonacci_dp function
def test_fibonacci_dp_0():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_1():
    assert fibonacci_dp(1) == 1

def test_fibonacci_dp_5():
    assert fibonacci_dp(5) == 5

def test_fibonacci_dp_negative():
    assert fibonacci_dp(-10) == 0

# Test cases for fibonacci_recursive function
def test_fibonacci_recursive_0():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_1():
    assert fibonacci_recursive(1) == 1

def test_fibonacci_recursive_5():
    assert fibonacci_recursive(5) == 5

def test_fibonacci_recursive_negative():
    assert fibonacci_recursive(-10) == 0