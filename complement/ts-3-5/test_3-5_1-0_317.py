import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from complement import complement

def test_complement_zero():
    assert complement(0) == 1

def test_complement_single_bit():
    assert complement(1) == 0

def test_complement_even_number():
    assert complement(6) == 1

def test_complement_odd_number():
    assert complement(5) == 2

def test_complement_large_number():
    assert complement(100) == 27