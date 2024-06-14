import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import fibonacci

import pytest

# Test Cases for fibonacci_dp function
def test_fibonacci_dp_zero():
    assert fibonacci.fibonacci_dp(0) == 0

def test_fibonacci_dp_one():
    assert fibonacci.fibonacci_dp(1) == 1

def test_fibonacci_dp_positive():
    assert fibonacci.fibonacci_dp(6) == 8

# Test Cases for fibonacci_recursive function
def test_fibonacci_recursive_zero():
    assert fibonacci.fibonacci_recursive(0) == 0

def test_fibonacci_recursive_one():
    assert fibonacci.fibonacci_recursive(1) == 1

def test_fibonacci_recursive_positive():
    assert fibonacci.fibonacci_recursive(6) == 8