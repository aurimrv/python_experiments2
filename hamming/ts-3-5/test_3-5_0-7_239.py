import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hamming_ops import hamming_distance, hamming_weight

def test_hamming_distance_equal_numbers():
    assert hamming_distance(5, 5) == 0

def test_hamming_distance_different_numbers():
    assert hamming_distance(4, 7) == 2

def test_hamming_distance_negative_numbers():
    assert hamming_distance(-2, -5) == 2

def test_hamming_weight_zero():
    assert hamming_weight(0) == 0

def test_hamming_weight_positive_number():
    assert hamming_weight(10) == 2

def test_hamming_weight_negative_number():
    assert hamming_weight(-7) == 4