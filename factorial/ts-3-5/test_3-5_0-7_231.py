import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

import pytest

# Test cases for the factorial function

def test_factorial_zero():
    assert factorial(0) == 0

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_negative():
    assert factorial(-5) == 0

def test_factorial_large():
    assert factorial(10) == 3628800