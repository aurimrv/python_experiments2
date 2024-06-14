import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

def test_factorial_with_positive_number():
    assert factorial(5) == 120
    assert factorial(6) == 720

def test_factorial_with_zero():
    assert factorial(0) == 0

def test_factorial_with_negative_number():
    assert factorial(-1) == 0