import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from radixsort import radixsort

import pytest

@pytest.mark.parametrize("input_list, expected_output", [
    ([3, 2, 1], [1, 2, 3]),
    ([5, 2, 9, 3, 6], [2, 3, 5, 6, 9]),
    ([100, 20, 345, 13, 87], [13, 20, 87, 100, 345]),
])
def test_radixsort(input_list, expected_output):
    assert radixsort(input_list) == expected_output

def test_radixsort_empty_list():
    with pytest.raises(ValueError):
        radixsort([])

def test_radixsort_single_element():
    assert radixsort([5]) == [5]

def test_radixsort_already_sorted():
    assert radixsort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_radixsort_reverse_order():
    assert radixsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_radixsort_duplicates():
    assert radixsort([3, 5, 2, 3, 5]) == [2, 3, 3, 5, 5]