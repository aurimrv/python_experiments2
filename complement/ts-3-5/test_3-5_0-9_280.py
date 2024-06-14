import os, sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import complement

def test_complement_zero_input():
    assert complement.complement(0) == 1

def test_complement_positive_input():
    assert complement.complement(5) == 2

def test_complement_negative_input():
    assert complement.complement(-7) == -7

def test_complement_large_input():
    assert complement.complement(100) == 27