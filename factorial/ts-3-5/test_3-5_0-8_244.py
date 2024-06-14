import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

def test_factorial_with_zero_input():
    assert factorial(0) == 0

def test_factorial_with_positive_input():
    assert factorial(5) == 120

def test_factorial_with_negative_input():
    assert factorial(-5) == 0

def test_factorial_with_large_input():
    assert factorial(10) == 3628800

def test_factorial_with_one_input():
    assert factorial(1) == 1