import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import pytest
from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix_empty_input():
    assert find_longest_common_prefix([]) == ''

def test_find_longest_common_prefix_same_word():
    assert find_longest_common_prefix(['apple', 'apple', 'apple']) == 'apple'

def test_find_longest_common_prefix_general_case():
    assert find_longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'

def test_find_longest_common_prefix_reduce_empty_input():
    assert find_longest_common_prefix_reduce([]) == ''

def test_find_longest_common_prefix_reduce_same_word():
    assert find_longest_common_prefix_reduce(['apple', 'apple', 'apple']) == 'apple'

def test_find_longest_common_prefix_reduce_general_case():
    assert find_longest_common_prefix_reduce(['flower', 'flow', 'flight']) == 'fl'