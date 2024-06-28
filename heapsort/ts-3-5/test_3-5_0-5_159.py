import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heapsort import heap_sort, max_heap_sort, custom_heap_sort

import pytest
from copy import deepcopy
from heapq import heapify, heappop

@pytest.mark.parametrize("input_list, expected_output", [
    ([4, 2, 1, 5, 3], [1, 2, 3, 4, 5]),
    ([9, 3, 7, 1, 5], [1, 3, 5, 7, 9]),
])
def test_heap_sort(input_list, expected_output):
    assert heap_sort(input_list) == expected_output

@pytest.mark.parametrize("input_list, expected_output", [
    ([4, 2, 1, 5, 3], [5, 4, 3, 2, 1]),
    ([9, 3, 7, 1, 5], [9, 7, 5, 3, 1]),
])
def test_max_heap_sort(input_list, expected_output):
    assert max_heap_sort(input_list) == expected_output

@pytest.mark.parametrize("input_list, sort, expected_output", [
    ([4, 2, 1, 5, 3], 'min', [1, 2, 3, 4, 5]),
    ([9, 3, 7, 1, 5], 'max', [9, 7, 5, 3, 1]),
])
def test_custom_heap_sort(input_list, sort, expected_output):
    assert custom_heap_sort(input_list, sort) == expected_output