import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

import pytest

def test_hamming_distance():
    assert hamming_distance(0b1101, 0b1001) == 1
    assert hamming_distance(0b1111, 0b0000) == 4
    assert hamming_distance(0b1010, 0b1010) == 0

def test_hamming_weight():
    assert hamming_weight(0b1101) == 3
    assert hamming_weight(0b11111111) == 8
    assert hamming_weight(0b1000) == 1