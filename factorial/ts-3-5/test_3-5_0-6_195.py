import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

import pytest

def test_factorial_with_zero():
    assert factorial(0) == 0

def test_factorial_with_positive_number():
    assert factorial(5) == 120

def test_factorial_with_negative_number():
    assert factorial(-5) == 0

def test_factorial_with_one():
    assert factorial(1) == 1

def test_factorial_with_large_number():
    assert factorial(10) == 3628800

def test_factorial_with_float():
    with pytest.raises(TypeError):
        factorial(2.5)

def test_factorial_with_string():
    with pytest.raises(TypeError):
        factorial("test")