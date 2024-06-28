import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from heapsort import heap_sort, max_heap_sort, custom_heap_sort

import pytest
from copy import deepcopy

@pytest.mark.parametrize("input_list, expected_output", [
    ([4, 2, 8, 1, 5], [1, 2, 4, 5, 8]),
    ([-3, 0, 7, -1, 2], [-3, -1, 0, 2, 7]),
])
def test_heap_sort(input_list, expected_output):
    assert heap_sort(input_list) == expected_output

@pytest.mark.parametrize("input_list, expected_output", [
    ([4, 2, 8, 1, 5], [8, 5, 4, 2, 1]),
    ([-3, 0, 7, -1, 2], [7, 2, 0, -1, -3]),
])
def test_max_heap_sort(input_list, expected_output):
    assert max_heap_sort(input_list) == expected_output

@pytest.mark.parametrize("input_list, sort, expected_output", [
    ([4, 2, 8, 1, 5], 'min', [1, 2, 4, 5, 8]),
    ([4, 2, 8, 1, 5], 'max', [8, 5, 4, 2, 1]),
    ([-3, 0, 7, -1, 2], 'min', [-3, -1, 0, 2, 7]),
    ([-3, 0, 7, -1, 2], 'max', [7, 2, 0, -1, -3]),
])
def test_custom_heap_sort(input_list, sort, expected_output):
    assert custom_heap_sort(input_list, sort) == expected_output