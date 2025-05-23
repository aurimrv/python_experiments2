import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

import pytest

def test_hamming_distance():
    assert hamming_distance(0, 0) == 0
    assert hamming_distance(1, 2) == 2
    assert hamming_distance(7, 7) == 0
    assert hamming_distance(15, 0) == 4

def test_hamming_weight():
    assert hamming_weight(0) == 0
    assert hamming_weight(1) == 1
    assert hamming_weight(7) == 3
    assert hamming_weight(15) == 4