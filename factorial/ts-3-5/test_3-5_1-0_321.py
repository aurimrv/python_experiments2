import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

def test_factorial_base_case():
    assert factorial(0) == 0

def test_factorial_negative_input():
    assert factorial(-5) == 0

def test_factorial_positive_integer():
    assert factorial(5) == 120

def test_factorial_large_integer():
    assert factorial(10) == 3628800