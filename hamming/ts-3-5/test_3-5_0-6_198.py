import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

import pytest

def test_hamming_distance():
    assert hamming_distance(1, 4) == 2
    assert hamming_distance(5, 5) == 0
    assert hamming_distance(10, 15) == 2

def test_hamming_weight():
    assert hamming_weight(4) == 1
    assert hamming_weight(5) == 2
    assert hamming_weight(255) == 8