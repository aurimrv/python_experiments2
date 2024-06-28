import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

def test_hamming_distance():
    # Test hamming_distance with equal numbers
    assert hamming_distance(5, 5) == 0

    # Test hamming_distance with one bit difference
    assert hamming_distance(5, 7) == 1

    # Test hamming_distance with completely different numbers
    assert hamming_distance(0, 15) == 4

def test_hamming_weight():
    # Test hamming_weight for 0
    assert hamming_weight(0) == 0

    # Test hamming_weight for a positive number
    assert hamming_weight(10) == 2

    # Test hamming_weight for a negative number
    assert hamming_weight(-10) == 3