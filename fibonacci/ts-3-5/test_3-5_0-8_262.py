import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

# Test Cases for fibonacci_dp function
def test_fibonacci_dp_zero():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_positive_number():
    assert fibonacci_dp(5) == 5

def test_fibonacci_dp_negative_number():
    assert fibonacci_dp(-3) == 0

# Test Cases for fibonacci_recursive function
def test_fibonacci_recursive_zero():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_positive_number():
    assert fibonacci_recursive(6) == 8

def test_fibonacci_recursive_negative_number():
    assert fibonacci_recursive(-4) == 0