import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

import pytest

# Tests for find_longest_common_prefix method
def test_find_longest_common_prefix_empty():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_all_same():
    words = ['apple', 'apple', 'apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_general_case():
    words = ['apple', 'app', 'apex']
    assert find_longest_common_prefix(words) == 'ap'

# Tests for find_longest_common_prefix_reduce method
def test_find_longest_common_prefix_reduce_empty():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_all_same():
    words = ['apple', 'apple', 'apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_general_case():
    words = ['apple', 'app', 'apex']
    assert find_longest_common_prefix_reduce(words) == 'ap'

def test_find_longest_common_prefix_reduce_different_lengths():
    words = ['apple', 'appl', 'ap']
    assert find_longest_common_prefix_reduce(words) == 'ap'