import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Test cases for find_longest_common_prefix method
def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_same_words():
    words = ['apple', 'apple', 'apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_different_words():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix(words) == ''

# Test cases for find_longest_common_prefix_reduce method
def test_find_longest_common_prefix_reduce_empty_list():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_same_words():
    words = ['apple', 'apple', 'apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_different_words():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix_reduce(words) == ''