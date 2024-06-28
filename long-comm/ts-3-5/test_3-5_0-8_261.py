import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    words = ['flower', 'flow', 'flight']
    assert find_longest_common_prefix(words) == 'fl'

def test_find_longest_common_prefix_empty_input():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['testing']
    assert find_longest_common_prefix(words) == 'testing'

def test_find_longest_common_prefix_reduce():
    words = ['flower', 'flow', 'flight']
    assert find_longest_common_prefix_reduce(words) == 'fl'

def test_find_longest_common_prefix_reduce_empty_input():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['testing']
    assert find_longest_common_prefix_reduce(words) == 'testing'