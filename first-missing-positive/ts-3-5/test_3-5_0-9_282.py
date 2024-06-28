import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

# Test cases for the first_missing_positive function

def test_first_missing_positive_case_1():
    assert first_missing_positive([1, 2, 0]) == 3

def test_first_missing_positive_case_2():
    assert first_missing_positive([3, 4, -1, 1]) == 2

def test_first_missing_positive_case_3():
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1

def test_first_missing_positive_case_4():
    assert first_missing_positive([1, 2, 3, 4]) == 5

def test_first_missing_positive_case_5():
    assert first_missing_positive([-1, -2, -3]) == 1

def test_first_missing_positive_case_6():
    assert first_missing_positive([1, 1, 1]) == 2