import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import complement

def test_complement_zero():
    assert complement.complement(0) == 1

def test_complement_one():
    assert complement.complement(1) == 0

def test_complement_positive():
    assert complement.complement(5) == 2

def test_complement_large_number():
    assert complement.complement(100) == 27