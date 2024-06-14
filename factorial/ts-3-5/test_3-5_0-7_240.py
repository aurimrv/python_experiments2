import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

import pytest

def test_factorial_zero():
    assert factorial(0) == 0

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_negative_input():
    assert factorial(-5) == 0

def test_factorial_large_input():
    assert factorial(10) == 3628800

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_two():
    assert factorial(2) == 2

def test_factorial_edge_case():
    assert factorial(20) == 2432902008176640000