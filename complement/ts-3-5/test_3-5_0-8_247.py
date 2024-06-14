import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from complement import complement

import pytest

@pytest.mark.parametrize("num, expected", [
    (0, 1),
    (1, 0),
    (2, 1),
    (3, 0),
    (4, 3),
    (5, 2),
    (6, 1),
    (7, 0),
    (8, 7),
])
def test_complement(num, expected):
    assert complement(num) == expected

def test_complement_large_number():
    assert complement(1000) == 23