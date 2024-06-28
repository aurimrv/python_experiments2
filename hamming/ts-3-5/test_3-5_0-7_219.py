import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

def test_hamming_distance():
    assert hamming_distance(1, 4) == 2

def test_hamming_distance_same_numbers():
    assert hamming_distance(3, 3) == 0

def test_hamming_weight():
    assert hamming_weight(7) == 3

def test_hamming_weight_negative_number():
    assert hamming_weight(-7) == 4
