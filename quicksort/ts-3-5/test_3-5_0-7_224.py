import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

from quicksort import quicksort

def test_quicksort():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_sort():
    assert quicksort([1]) == [1]
    assert quicksort([]) == []

def test_partition():
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert quicksort([5, 9, 2, 6, 5]) == [2, 5, 5, 6, 9]