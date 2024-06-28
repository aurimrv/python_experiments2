import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

import pytest

# Test cases for hamming_distance method
def test_hamming_distance_different_numbers():
    assert hamming_distance(1, 2) == 2

def test_hamming_distance_same_numbers():
    assert hamming_distance(3, 3) == 0

# Test cases for hamming_weight method
def test_hamming_weight_positive_number():
    assert hamming_weight(7) == 3

def test_hamming_weight_negative_number():
    assert hamming_weight(-7) == 4