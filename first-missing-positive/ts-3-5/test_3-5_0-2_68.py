import os
import sys
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
    assert first_missing_positive([1, 2, 2, 1]) == 3

def test_first_missing_positive_negative_values():
    assert first_missing_positive([-1, -2, -3]) == 1

def test_first_missing_positive_empty_list():
    assert first_missing_positive([]) == 1

def test_first_missing_positive_large_values():
    assert first_missing_positive([1000, 1001, 1002]) == 1