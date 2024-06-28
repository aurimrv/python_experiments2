import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Test cases for find_longest_common_prefix function
def test_find_longest_common_prefix_empty_input():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_same_word():
    words = ['apple', 'apple', 'apple']
    assert find_longest_common_prefix(words) == 'apple'

# Test cases for find_longest_common_prefix_reduce function
def test_find_longest_common_prefix_reduce_empty_input():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_same_word():
    words = ['banana', 'banana', 'banana']
    assert find_longest_common_prefix_reduce(words) == 'banana'