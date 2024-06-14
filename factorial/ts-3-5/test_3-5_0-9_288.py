import os
import sys
import pytest

# Add project directory to sys path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

def test_factorial_positive_input():
    assert factorial(0) == 0
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_negative_input():
    assert factorial(-1) == 0
    assert factorial(-5) == 0

def test_factorial_large_input():
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000

def test_factorial_string_input():
    with pytest.raises(TypeError):
        factorial("test")

def test_factorial_float_input():
    with pytest.raises(TypeError):
        factorial(5.5)