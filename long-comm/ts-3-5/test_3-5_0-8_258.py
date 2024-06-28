import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix_empty_list():
    assert find_longest_common_prefix([]) == ''
    assert find_longest_common_prefix_reduce([]) == ''

def test_find_longest_common_prefix_single_word():
    assert find_longest_common_prefix(['apple']) == 'apple'
    assert find_longest_common_prefix_reduce(['apple']) == 'apple'

def test_find_longest_common_prefix_all_same_words():
    assert find_longest_common_prefix(['banana', 'banana', 'banana']) == 'banana'
    assert find_longest_common_prefix_reduce(['banana', 'banana', 'banana']) == 'banana'

def test_find_longest_common_prefix_different_lengths():
    assert find_longest_common_prefix(['car', 'cars', 'cart']) == 'car'
    assert find_longest_common_prefix_reduce(['car', 'cars', 'cart']) == 'car'

def test_find_longest_common_prefix_general_case():
    assert find_longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
    assert find_longest_common_prefix_reduce(['flower', 'flow', 'flight']) == 'fl'