import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive_empty_list():
    assert first_missing_positive([]) == 1

def test_first_missing_positive_single_element_list():
    assert first_missing_positive([1]) == 2

def test_first_missing_positive_all_negative_numbers():
    assert first_missing_positive([-5, -10, -3, -1]) == 1

def test_first_missing_positive_all_positive_numbers_in_sequence():
    assert first_missing_positive([1, 2, 3, 4]) == 5

def test_first_missing_positive_missing_number_in_sequence():
    assert first_missing_positive([3, 4, -1, 1]) == 2