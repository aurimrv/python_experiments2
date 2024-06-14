import os
import sys
from functools import reduce

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import factorial

def test_factorial_with_0():
    assert factorial.factorial(0) == 0

def test_factorial_with_positive_number():
    assert factorial.factorial(5) == 120

def test_factorial_of_1():
    assert factorial.factorial(1) == 1

def test_factorial_of_2():
    assert factorial.factorial(2) == 2

def test_factorial_of_10():
    assert factorial.factorial(10) == 3628800

def test_factorial_of_negative_number():
    assert factorial.factorial(-5) == 0