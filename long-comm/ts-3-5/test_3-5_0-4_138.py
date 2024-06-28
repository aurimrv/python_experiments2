import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Test cases for find_longest_common_prefix
def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_no_common_prefix():
    words = ['dog', 'cat', 'bird']
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_common_prefix():
    words = ['flower', 'flow', 'flight']
    assert find_longest_common_prefix(words) == 'fl'

# Test cases for find_longest_common_prefix_reduce
def test_find_longest_common_prefix_reduce_empty_list():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_no_common_prefix():
    words = ['dog', 'cat', 'bird']
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_common_prefix():
    words = ['flower', 'flow', 'flight']
    assert find_longest_common_prefix_reduce(words) == 'fl'