import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from complement import complement

import pytest

# Test cases for the `complement` function
def test_zero_input():
    assert complement(0) == 1

def test_even_input():
    assert complement(2) == 1

def test_odd_input():
    assert complement(5) == 2

def test_power_of_2_input():
    assert complement(4) == 3

def test_large_input():
    assert complement(100) == 27