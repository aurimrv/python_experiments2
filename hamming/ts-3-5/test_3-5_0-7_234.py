import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

def test_hamming_distance():
    assert hamming_distance(0, 0) == 0
    assert hamming_distance(1, 1) == 0
    assert hamming_distance(3, 5) == 2
    assert hamming_distance(7, 0) == 3

def test_hamming_weight():
    assert hamming_weight(0) == 0
    assert hamming_weight(1) == 1
    assert hamming_weight(255) == 8
    assert hamming_weight(-1) == 2
    assert hamming_weight(-5) == 3