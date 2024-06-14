import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from complement import complement

def test_complement_all_zeros():
    assert complement(0) == 1

def test_complement_single_bit():
    assert complement(1) == 0

def test_complement_multi_bit_even():
    assert complement(6) == 1

def test_complement_multi_bit_odd():
    assert complement(5) == 2