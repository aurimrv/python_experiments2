import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
sys.setrecursionlimit(15000)

# Import the file to be tested after setting up the paths
import quicksort

def test_quicksort_empty_list():
    ar = []
    sorted_ar = quicksort.quicksort(ar)
    assert sorted_ar == []

def test_quicksort_single_element():
    ar = [5]
    sorted_ar = quicksort.quicksort(ar)
    assert sorted_ar == [5]

def test_quicksort_sorted_list():
    ar = [1, 2, 3, 4, 5]
    sorted_ar = quicksort.quicksort(ar)
    assert sorted_ar == [1, 2, 3, 4, 5]

def test_quicksort_reverse_sorted_list():
    ar = [5, 4, 3, 2, 1]
    sorted_ar = quicksort.quicksort(ar)
    assert sorted_ar == [1, 2, 3, 4, 5]

def test_quicksort_random_list():
    ar = [3, 7, 1, 9, 2, 5]
    sorted_ar = quicksort.quicksort(ar)
    assert sorted_ar == [1, 2, 3, 5, 7, 9]