import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from factorial import factorial

def test_factorial():
    assert factorial(0) == 0

def test_factorial_positive():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120

def test_factorial_negative():
    assert factorial(-1) == 0

def test_factorial_large_number():
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000