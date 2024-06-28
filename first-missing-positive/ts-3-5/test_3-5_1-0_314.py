import sys
import os
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_sorted():
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

def test_first_missing_positive_unsorted():
    assert first_missing_positive([3, 4, -1, 1]) == 2

def test_first_missing_positive_duplicates():
    assert first_missing_positive([1, 1, 2, 3, 4]) == 5

def test_first_missing_positive_single_element():
    assert first_missing_positive([5]) == 1

def test_first_missing_positive_all_negatives():
    assert first_missing_positive([-1, -2, -3, -4]) == 1

def test_first_missing_positive_large_input():
    assert first_missing_positive([9, 7, 8, 3, 1, 2, 6, 5, 4, 10]) == 11