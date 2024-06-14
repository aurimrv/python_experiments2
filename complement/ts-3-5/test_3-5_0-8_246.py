import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import complement

def test_complement_zero_input():
    assert complement.complement(0) == 1

def test_complement_positive_input():
    assert complement.complement(5) == 2
    assert complement.complement(10) == 5