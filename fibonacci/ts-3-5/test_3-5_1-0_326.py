import pytest
import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fibonacci import fibonacci_dp, fibonacci_recursive

# Test Cases for fibonacci_dp
def test_fibonacci_dp_when_target_is_0():
    assert fibonacci_dp(0) == 0

def test_fibonacci_dp_when_target_is_1():
    assert fibonacci_dp(1) == 1

def test_fibonacci_dp_when_target_is_5():
    assert fibonacci_dp(5) == 5

def test_fibonacci_dp_when_target_is_negative():
    assert fibonacci_dp(-5) == 0

# Test Cases for fibonacci_recursive
def test_fibonacci_recursive_when_target_is_0():
    assert fibonacci_recursive(0) == 0

def test_fibonacci_recursive_when_target_is_1():
    assert fibonacci_recursive(1) == 1

def test_fibonacci_recursive_when_target_is_5():
    assert fibonacci_recursive(5) == 5

def test_fibonacci_recursive_when_target_is_negative():
    assert fibonacci_recursive(-5) == 0