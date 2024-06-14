import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

def test_factorial_positive_input():
    assert factorial(5) == 120
    assert factorial(7) == 5040

def test_factorial_zero_input():
    assert factorial(0) == 0

def test_factorial_negative_input():
    assert factorial(-5) == 0

def test_factorial_large_input():
    assert factorial(10) == 3628800
    assert factorial(15) == 1307674368000