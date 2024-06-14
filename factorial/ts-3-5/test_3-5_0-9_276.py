import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

import pytest

def test_factorial_of_0():
    assert factorial(0) == 0

def test_factorial_of_1():
    assert factorial(1) == 1

def test_factorial_of_positive_number():
    assert factorial(5) == 120

def test_factorial_of_negative_number():
    assert factorial(-1) == 0

def test_factorial_of_large_number():
    assert factorial(10) == 3628800