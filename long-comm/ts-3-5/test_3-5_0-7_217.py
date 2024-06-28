import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix_empty_input():
    assert find_longest_common_prefix([]) == ''
    assert find_longest_common_prefix_reduce([]) == ''

def test_find_longest_common_prefix_single_word():
    assert find_longest_common_prefix(['apple']) == 'apple'
    assert find_longest_common_prefix_reduce(['apple']) == 'apple'

def test_find_longest_common_prefix_multiple_words():
    assert find_longest_common_prefix(['apple', 'ape', 'apartment']) == 'ap'
    assert find_longest_common_prefix_reduce(['apple', 'ape', 'apartment']) == 'ap'

def test_find_longest_common_prefix_no_common_prefix():
    assert find_longest_common_prefix(['apple', 'banana', 'cherry']) == ''
    assert find_longest_common_prefix_reduce(['apple', 'banana', 'cherry']) == ''

def test_find_longest_common_prefix_reduce_shorter_word():
    assert find_longest_common_prefix_reduce(['apple', 'appl']) == 'appl'
    assert find_longest_common_prefix_reduce(['apple', 'ap']) == 'ap'