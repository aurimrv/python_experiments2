import sys
import os
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Test cases for find_longest_common_prefix function
def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['testing']
    assert find_longest_common_prefix(words) == 'testing'

def test_find_longest_common_prefix_same_words():
    words = ['apple', 'apple', 'apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_non_matching_words():
    words = ['apple', 'banana', 'cat']
    assert find_longest_common_prefix(words) == ''

# Test cases for find_longest_common_prefix_reduce function
def test_find_longest_common_prefix_reduce_empty_list():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['testing']
    assert find_longest_common_prefix_reduce(words) == 'testing'

def test_find_longest_common_prefix_reduce_same_words():
    words = ['apple', 'apple', 'apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_non_matching_words():
    words = ['apple', 'banana', 'cat']
    assert find_longest_common_prefix_reduce(words) == ''