import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

import pytest

# Test cases for find_longest_common_prefix method
def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_all_same_words():
    words = ['banana', 'banana', 'banana']
    assert find_longest_common_prefix(words) == 'banana'

def test_find_longest_common_prefix_different_words():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_long_prefix():
    words = ['apple', 'apples', 'applet']
    assert find_longest_common_prefix(words) == 'apple'

# Test cases for find_longest_common_prefix_reduce method
def test_find_longest_common_prefix_reduce_empty_list():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_all_same_words():
    words = ['banana', 'banana', 'banana']
    assert find_longest_common_prefix_reduce(words) == 'banana'

def test_find_longest_common_prefix_reduce_different_words():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_long_prefix():
    words = ['apple', 'apples', 'applet']
    assert find_longest_common_prefix_reduce(words) == 'apple'