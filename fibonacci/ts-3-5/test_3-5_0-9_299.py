import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

# Test cases for fibonacci_dp function
def test_fibonacci_dp_with_positive_number():
    assert fibonacci_dp(5) == 5

def test_fibonacci_dp_with_zero():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_with_negative_number():
    assert fibonacci_dp(-1) == 0

# Test cases for fibonacci_recursive function
def test_fibonacci_recursive_with_positive_number():
    assert fibonacci_recursive(5) == 5
    
def test_fibonacci_recursive_with_zero():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_with_negative_number():
    assert fibonacci_recursive(-1) == 0