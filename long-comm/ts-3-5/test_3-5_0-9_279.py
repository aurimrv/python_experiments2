import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix_empty_input():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_multiple_words_same_prefix():
    words = ['apple', 'applet', 'applepie']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_multiple_words_different_prefix():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_reduce_empty_input():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_multiple_words_same_prefix():
    words = ['apple', 'applet', 'applepie']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_multiple_words_different_prefix():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix_reduce(words) == ''