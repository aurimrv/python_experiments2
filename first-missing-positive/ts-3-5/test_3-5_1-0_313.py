import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from first_missing_positive import first_missing_positive

def test_first_missing_positive():
    assert first_missing_positive([1, 2, 0]) == 3

def test_first_missing_positive_with_duplicate():
    assert first_missing_positive([3, 4, -1, 1]) == 2

def test_first_missing_positive_with_negative_numbers():
    assert first_missing_positive([-1, -2, 0]) == 1

def test_first_missing_positive_with_out_of_order_numbers():
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1

def test_first_missing_positive_with_sorted_list():
    assert first_missing_positive([1, 2, 3, 4]) == 5