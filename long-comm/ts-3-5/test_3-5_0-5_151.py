import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Test cases for find_longest_common_prefix method
def test_find_longest_common_prefix_empty_list():
    assert find_longest_common_prefix([]) == ''

def test_find_longest_common_prefix_single_word():
    assert find_longest_common_prefix(['apple']) == 'apple'

def test_find_longest_common_prefix_same_words():
    assert find_longest_common_prefix(['banana', 'banana', 'banana']) == 'banana'

def test_find_longest_common_prefix_general_case():
    assert find_longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'

# Test cases for find_longest_common_prefix_reduce method
def test_find_longest_common_prefix_reduce_empty_list():
    assert find_longest_common_prefix_reduce([]) == ''

def test_find_longest_common_prefix_reduce_single_word():
    assert find_longest_common_prefix_reduce(['apple']) == 'apple'

def test_find_longest_common_prefix_reduce_same_words():
    assert find_longest_common_prefix_reduce(['banana', 'banana', 'banana']) == 'banana'

def test_find_longest_common_prefix_reduce_general_case():
    assert find_longest_common_prefix_reduce(['flower', 'flow', 'flight']) == 'fl'