import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

# Tests for fibonacci_dp function
def test_fibonacci_dp_zero():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_one():
    assert fibonacci_dp(1) == 1

def test_fibonacci_dp_positive():
    assert fibonacci_dp(5) == 5

def test_fibonacci_dp_negative():
    assert fibonacci_dp(-5) == 0

# Tests for fibonacci_recursive function
def test_fibonacci_recursive_zero():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_one():
    assert fibonacci_recursive(1) == 1

def test_fibonacci_recursive_positive():
    assert fibonacci_recursive(5) == 5

def test_fibonacci_recursive_negative():
    assert fibonacci_recursive(-5) == 0