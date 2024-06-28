import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    assert first_missing_positive([1, 2, 0]) == 3

def test_first_missing_positive_empty():
    assert first_missing_positive([]) == 1

def test_first_missing_positive_negative():
    assert first_missing_positive([-1, -2, -3]) == 1

def test_first_missing_positive_duplicates():
    assert first_missing_positive([1, 1, 3]) == 2

def test_first_missing_positive_large_numbers():
    assert first_missing_positive([1000, 1001, 1002]) == 1