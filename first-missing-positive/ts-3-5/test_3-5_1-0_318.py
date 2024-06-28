import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_example1():
    assert first_missing_positive([3, 4, -1, 1]) == 2

def test_first_missing_positive_example2():
    assert first_missing_positive([1, 2, 0]) == 3

def test_first_missing_positive_single_element():
    assert first_missing_positive([1]) == 2

def test_first_missing_positive_all_negative():
    assert first_missing_positive([-1, -2, -3]) == 1

def test_first_missing_positive_duplicates():
    assert first_missing_positive([1, 1, 2, 2, 3, 3]) == 4

def test_first_missing_positive_start_greater_than_end():
    assert first_missing_positive([4, 5, 6, 7]) == 1

def test_first_missing_positive_large_input():
    assert first_missing_positive(list(range(1, 1000000))) == 1000000