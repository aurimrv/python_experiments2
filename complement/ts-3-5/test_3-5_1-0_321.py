import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from complement import complement

import pytest

def test_complement_zero_input():
    assert complement(0) == 1

def test_complement_odd_input():
    assert complement(5) == 2
    assert complement(7) == 0

def test_complement_even_input():
    assert complement(8) == 7
    assert complement(10) == 5