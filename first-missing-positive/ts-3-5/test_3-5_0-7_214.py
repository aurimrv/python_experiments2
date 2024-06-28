import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import pytest
from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1

def test_first_missing_positive_duplicates():
    assert first_missing_positive([1, 1, 1]) == 2
    assert first_missing_positive([2, 2, 2]) == 1

def test_first_missing_positive_negative_numbers():
    assert first_missing_positive([-1, -2, -3]) == 1
    assert first_missing_positive([-3, -2, -1, 0]) == 1

def test_first_missing_positive_large_lists():
    assert first_missing_positive(list(range(1, 1001))) == 1001
    assert first_missing_positive(list(range(2, 1001))) == 1