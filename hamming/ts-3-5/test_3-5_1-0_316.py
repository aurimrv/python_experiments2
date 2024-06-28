import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import hamming_ops

def test_hamming_distance():
    assert hamming_ops.hamming_distance(0, 0) == 0
    assert hamming_ops.hamming_distance(1, 2) == 2
    assert hamming_ops.hamming_distance(7, 7) == 0
    assert hamming_ops.hamming_distance(8, 3) == 3

def test_hamming_weight():
    assert hamming_ops.hamming_weight(0) == 0
    assert hamming_ops.hamming_weight(5) == 2
    assert hamming_ops.hamming_weight(255) == 8
    assert hamming_ops.hamming_weight(16) == 1