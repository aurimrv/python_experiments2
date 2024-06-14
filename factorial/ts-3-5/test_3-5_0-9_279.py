import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

def test_factorial_with_zero():
    result = factorial(0)
    assert result == 0

def test_factorial_with_positive_number():
    result = factorial(5)
    assert result == 120

def test_factorial_with_negative_number():
    result = factorial(-5)
    assert result == 0

def test_factorial_of_one():
    result = factorial(1)
    assert result == 1