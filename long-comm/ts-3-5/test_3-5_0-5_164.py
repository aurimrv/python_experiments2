import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

import pytest

# Test cases for find_longest_common_prefix method
def test_find_longest_common_prefix_empty_list():
    assert find_longest_common_prefix([]) == ''

def test_find_longest_common_prefix_single_word():
    assert find_longest_common_prefix(['apple']) == 'apple'

def test_find_longest_common_prefix_no_common_prefix():
    assert find_longest_common_prefix(['dog', 'cat', 'bird']) == ''

def test_find_longest_common_prefix_common_prefix():
    assert find_longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'

# Test cases for find_longest_common_prefix_reduce method
def test_find_longest_common_prefix_reduce_empty_list():
    assert find_longest_common_prefix_reduce([]) == ''

def test_find_longest_common_prefix_reduce_single_word():
    assert find_longest_common_prefix_reduce(['apple']) == 'apple'

def test_find_longest_common_prefix_reduce_no_common_prefix():
    assert find_longest_common_prefix_reduce(['dog', 'cat', 'bird']) == ''

def test_find_longest_common_prefix_reduce_common_prefix():
    assert find_longest_common_prefix_reduce(['flower', 'flow', 'flight']) == 'fl'