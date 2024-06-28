import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix_empty():
    assert find_longest_common_prefix([]) == ''

def test_find_longest_common_prefix_single_word():
    assert find_longest_common_prefix(['apple']) == 'apple'

def test_find_longest_common_prefix_same_words():
    assert find_longest_common_prefix(['banana', 'banana', 'banana']) == 'banana'

def test_find_longest_common_prefix_no_common_prefix():
    assert find_longest_common_prefix(['dog', 'cat', 'bird']) == ''

def test_find_longest_common_prefix_reduce_empty():
    assert find_longest_common_prefix_reduce([]) == ''

def test_find_longest_common_prefix_reduce_single_word():
    assert find_longest_common_prefix_reduce(['apple']) == 'apple'

def test_find_longest_common_prefix_reduce_same_words():
    assert find_longest_common_prefix_reduce(['banana', 'banana', 'banana']) == 'banana'

def test_find_longest_common_prefix_reduce_no_common_prefix():
    assert find_longest_common_prefix_reduce(['dog', 'cat', 'bird']) == ''