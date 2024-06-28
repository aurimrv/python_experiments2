import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

import pytest

def test_hamming_distance_diff_bits():
    assert hamming_distance(2, 3) == 1

def test_hamming_distance_same_bits():
    assert hamming_distance(4, 4) == 0

def test_hamming_weight_positive_number():
    assert hamming_weight(7) == 3

def test_hamming_weight_negative_number():
    assert hamming_weight(-7) == 4

def test_hamming_weight_zero():
    assert hamming_weight(0) == 0