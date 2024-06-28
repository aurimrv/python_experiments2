import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Test cases for find_longest_common_prefix function
def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_all_different():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_common_prefix_present():
    words = ['apple', 'ape', 'apartment']
    assert find_longest_common_prefix(words) == 'ap'

def test_find_longest_common_prefix_reduce_empty_list():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_all_different():
    words = ['apple', 'banana', 'cherry']
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_common_prefix_present():
    words = ['apple', 'ape', 'apartment']
    assert find_longest_common_prefix_reduce(words) == 'ap'