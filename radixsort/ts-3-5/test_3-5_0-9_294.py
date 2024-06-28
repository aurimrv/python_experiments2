import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from radixsort import radixsort

import pytest

@pytest.mark.parametrize("ar, base, expected", [
    ([3, 2, 5, 1, 4], 10, [1, 2, 3, 4, 5]),  # Test sorting list of integers with base 10
    ([170, 45, 75, 90, 802, 24, 2, 66], 10, [2, 24, 45, 66, 75, 90, 170, 802]),  # Test sorting large list of integers with base 10
    ([543, 764, 245, 530, 345, 760, 555], 10, [245, 345, 530, 543, 555, 760, 764]),  # Test sorting list of different integers with base 10
])
def test_radixsort(ar, base, expected):
    assert radixsort(ar, base) == expected

@pytest.mark.parametrize("ar, base, expected", [
    ([3, 2, 5, 1, 4], 2, [1, 2, 3, 4, 5]),  # Test sorting list of integers with base 2
    ([170, 45, 75, 90, 802, 24, 2, 66], 16, [2, 24, 45, 66, 75, 90, 170, 802]),  # Test sorting large list of integers with base 16
    ([543, 764, 245, 530, 345, 760, 555], 8, [245, 345, 530, 543, 555, 760, 764]),  # Test sorting list of different integers with base 8
])
def test_radixsort_different_base(ar, base, expected):
    assert radixsort(ar, base) == expected