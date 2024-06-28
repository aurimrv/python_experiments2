import pytest
import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_multiple_words_same_prefix():
    words = ['apple', 'appletree', 'applesauce']
    assert find_longest_common_prefix(words) == 'apple'
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_multiple_words_no_common_prefix():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix(words) == ''
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_long_common_prefix():
    words = ['apple', 'appletree', 'applepie']
    assert find_longest_common_prefix(words) == 'apple'
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_no_common_prefix():
    words = ['dog', 'cat', 'bird']
    assert find_longest_common_prefix(words) == ''
    assert find_longest_common_prefix_reduce(words) == ''