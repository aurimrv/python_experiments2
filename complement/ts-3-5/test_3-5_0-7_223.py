import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from complement import complement

def test_complement_all_zeroes():
    assert complement(0) == 1

def test_complement_single_bit_set():
    assert complement(2) == 1

def test_complement_multiple_bits_set():
    assert complement(5) == 2

def test_complement_large_number():
    assert complement(15) == 0

def test_complement_negative_number():
    assert complement(-3) == -3

def test_complement_zero():
    assert complement(1) == 0