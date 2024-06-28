import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort

def test_quicksort():
    # Test case for an empty list
    assert quicksort([]) == []

    # Test case for a list with one element
    assert quicksort([5]) == [5]

    # Test case for a list with multiple elements in ascending order
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test case for a list with multiple elements in descending order
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Test case for a list with multiple elements in random order
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    # Test case for a list with duplicate elements
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 4, 1]) == [1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 9]