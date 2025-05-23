import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

import pytest

# Test cases for fibonacci_dp function
def test_fibonacci_dp_negative_input():
    assert fibonacci_dp(-5) == 0

def test_fibonacci_dp_zero_input():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_first_fibonacci_number():
    assert fibonacci_dp(1) == 1

def test_fibonacci_dp_second_fibonacci_number():
    assert fibonacci_dp(2) == 1

def test_fibonacci_dp_fifth_fibonacci_number():
    assert fibonacci_dp(5) == 5

# Test cases for fibonacci_recursive function
def test_fibonacci_recursive_negative_input():
    assert fibonacci_recursive(-5) == 0

def test_fibonacci_recursive_zero_input():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_first_fibonacci_number():
    assert fibonacci_recursive(1) == 1

def test_fibonacci_recursive_second_fibonacci_number():
    assert fibonacci_recursive(2) == 1

def test_fibonacci_recursive_fifth_fibonacci_number():
    assert fibonacci_recursive(5) == 5