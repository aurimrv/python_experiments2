import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heapsort import heap_sort, max_heap_sort, custom_heap_sort

import pytest
from copy import deepcopy

@pytest.mark.parametrize("input_list, expected_output", [
    ([3, 2, 1], [1, 2, 3]),
    ([5, 7, 2, 4, 1], [1, 2, 4, 5, 7]),
    ([9, 3, 6, 2, 8], [2, 3, 6, 8, 9])
])
def test_heap_sort(input_list, expected_output):
    assert heap_sort(input_list) == expected_output

@pytest.mark.parametrize("input_list, expected_output", [
    ([3, 2, 1], [3, 2, 1]),
    ([5, 7, 2, 4, 1], [7, 5, 4, 2, 1]),
    ([9, 3, 6, 2, 8], [9, 8, 6, 3, 2])
])
def test_max_heap_sort(input_list, expected_output):
    assert max_heap_sort(input_list) == expected_output

@pytest.mark.parametrize("input_list, sort, expected_output", [
    ([3, 2, 1], 'min', [1, 2, 3]),
    ([5, 7, 2, 4, 1], 'max', [7, 5, 4, 2, 1]),
    ([9, 3, 6, 2, 8], 'min', [2, 3, 6, 8, 9]),
    ([9, 3, 6, 2, 8], 'max', [9, 8, 6, 3, 2])
])
def test_custom_heap_sort(input_list, sort, expected_output):
    assert custom_heap_sort(input_list, sort) == expected_output