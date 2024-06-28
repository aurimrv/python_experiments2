import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Tests for find_longest_common_prefix() function
def test_find_longest_common_prefix_empty_input():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_common_prefix():
    words = ['apple', 'app', 'aptitude']
    assert find_longest_common_prefix(words) == 'ap'

def test_find_longest_common_prefix_no_common_prefix():
    words = ['hello', 'world', 'test']
    assert find_longest_common_prefix(words) == ''

# Tests for find_longest_common_prefix_reduce() function
def test_find_longest_common_prefix_reduce_empty_input():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_common_prefix():
    words = ['apple', 'app', 'aptitude']
    assert find_longest_common_prefix_reduce(words) == 'ap'

def test_find_longest_common_prefix_reduce_no_common_prefix():
    words = ['hello', 'world', 'test']
    assert find_longest_common_prefix_reduce(words) == ''