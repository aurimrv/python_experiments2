import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_empty_list():
    assert first_missing_positive([]) == 1

def test_first_missing_positive_single_element():
    assert first_missing_positive([1]) == 2

def test_first_missing_positive_sorted_list():
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

def test_first_missing_positive_unsorted_list():
    assert first_missing_positive([3, 4, -1, 1]) == 2

def test_first_missing_positive_with_duplicates():
    assert first_missing_positive([1, 1, 2, 3]) == 4

def test_first_missing_positive_with_negative_values():
    assert first_missing_positive([5, -1, -2, 1, 0]) == 2

def test_first_missing_positive_all_negative_values():
    assert first_missing_positive([-1, -2, -3]) == 1

def test_first_missing_positive_all_positive_values():
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6

def test_first_missing_positive_large_list():
    assert first_missing_positive([7, 8, 9, 11, 12, 13]) == 1