import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from complement import complement

import pytest

def test_complement_zero_input():
    assert complement(0) == 1

def test_complement_positive_input():
    assert complement(2) == 1
    assert complement(5) == 2

def test_complement_large_input():
    assert complement(15) == 0
    assert complement(10) == 5