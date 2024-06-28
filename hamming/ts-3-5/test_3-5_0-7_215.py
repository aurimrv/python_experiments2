import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

import pytest

def test_hamming_distance():
    # Test cases where both numbers are 0
    assert hamming_distance(0, 0) == 0
    assert hamming_distance(0, 0) == 0

    # Test cases where one number is 0 and the other is a non-zero number
    assert hamming_distance(0, 5) == 2
    assert hamming_distance(10, 0) == 2

    # Test cases where both numbers are the same
    assert hamming_distance(7, 7) == 0
    assert hamming_distance(15, 15) == 0

def test_hamming_weight():
    # Test cases where the number has all bits off
    assert hamming_weight(0) == 0
    assert hamming_weight(1) == 1

    # Test cases where the number has alternating bits
    assert hamming_weight(85) == 4
    assert hamming_weight(170) == 4

    # Test cases where the number has all bits on
    assert hamming_weight(255) == 8
    assert hamming_weight(65535) == 16