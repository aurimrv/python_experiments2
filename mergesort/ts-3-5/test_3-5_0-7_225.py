import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from mergesort import mergesort

import pytest

@pytest.mark.parametrize("input_list, expected_output", [
    ([4, 2, 7, 5, 1, 3, 6], [1, 2, 3, 4, 5, 6, 7]),
    ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]),
    ([-2, 0, 5, -1, 8, 3, 1, 6], [-2, -1, 0, 1, 3, 5, 6, 8]),
])
def test_mergesort(input_list, expected_output):
    assert mergesort(input_list) == expected_output

@pytest.mark.parametrize("input_list, expected_output", [
    ([], []),
    ([1], [1]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([2, 4, 6, 8, 10], [2, 4, 6, 8, 10]),
])
def test_mergesort_edge_cases(input_list, expected_output):
    assert mergesort(input_list) == expected_output