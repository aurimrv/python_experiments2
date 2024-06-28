import os
import sys
from collections import deque

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

def test_sort():
    assert mergesort([]) == []
    assert mergesort([3, 2, 1]) == [1, 2, 3]
    assert mergesort([5, 8, 1, 3, 6, 2, 7, 4]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_merge():
    assert mergesort([]) == []
    assert mergesort([1, 3, 5] + [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert mergesort([4, 7, 9] + [1, 2, 8]) == [1, 2, 4, 7, 8, 9]

def test_mergesort():
    assert mergesort([]) == []
    assert mergesort([3, 2, 1]) == [1, 2, 3]
    assert mergesort([5, 8, 1, 3, 6, 2, 7, 4]) == [1, 2, 3, 4, 5, 6, 7, 8]