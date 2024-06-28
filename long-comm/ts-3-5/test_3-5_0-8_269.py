import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

import pytest

# Test cases for find_longest_common_prefix

def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_no_common_prefix():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_common_prefix_present():
    words = ['apple', 'application', 'apricot']
    assert find_longest_common_prefix(words) == 'ap'

# Test cases for find_longest_common_prefix_reduce

def test_find_longest_common_prefix_reduce_empty_list():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_no_common_prefix():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_common_prefix_present():
    words = ['apple', 'application', 'apricot']
    assert find_longest_common_prefix_reduce(words) == 'ap'