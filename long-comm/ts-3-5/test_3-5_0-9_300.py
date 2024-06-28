import os
import sys
import pytest

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

def test_find_longest_common_prefix_equal_words():
    words = ['banana', 'banana', 'banana']
    assert find_longest_common_prefix(words) == 'banana'
    assert find_longest_common_prefix_reduce(words) == 'banana'

def test_find_longest_common_prefix_general_case():
    words = ['apple', 'appetizer', 'approve']
    assert find_longest_common_prefix(words) == 'app'
    assert find_longest_common_prefix_reduce(words) == 'app'

def test_find_longest_common_prefix_reduce_equal_words():
    words = ['pear', 'pear', 'pear']
    assert find_longest_common_prefix(words) == 'pear'
    assert find_longest_common_prefix_reduce(words) == 'pear'