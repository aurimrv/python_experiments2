import pytest
import os
import sys

# Add the project directory to sys.path for correct imports
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort

def test_quicksort_empty_list():
    # Verify sorting an empty list returns an empty list
    assert quicksort([]) == []

def test_quicksort_sorted_list():
    # Verify sorting a sorted list returns the same list
    sorted_list = [1, 2, 3, 4, 5]
    assert quicksort(sorted_list.copy()) == sorted_list

def test_quicksort_reversed_list():
    # Verify sorting a reversed list returns the list in ascending order
    reversed_list = [5, 4, 3, 2, 1]
    assert quicksort(reversed_list.copy()) == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    # Verify sorting a random list returns the list in ascending order
    random_list = [8, 3, 10, 1, 5]
    assert quicksort(random_list.copy()) == [1, 3, 5, 8, 10]

def test_quicksort_duplicate_values():
    # Verify sorting a list with duplicate values returns the list in ascending order
    duplicate_list = [3, 2, 1, 2, 3]
    assert quicksort(duplicate_list.copy()) == [1, 2, 2, 3, 3]