import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_no_common_prefix():
    words = ['dog', 'cat', 'horse']
    assert find_longest_common_prefix(words) == ''
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_common_prefix():
    words = ['flow', 'flower', 'flour']
    assert find_longest_common_prefix(words) == 'flo'
    assert find_longest_common_prefix_reduce(words) == 'flo'

def test_find_longest_common_prefix_different_lengths():
    words = ['car', 'cart', 'cartoon']
    assert find_longest_common_prefix(words) == 'car'
    assert find_longest_common_prefix_reduce(words) == 'car'

def test_find_longest_common_prefix_reduce_empty_list():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_no_common_prefix():
    words = ['dog', 'cat', 'horse']
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_common_prefix():
    words = ['flow', 'flower', 'flour']
    assert find_longest_common_prefix_reduce(words) == 'flo'

def test_find_longest_common_prefix_reduce_different_lengths():
    words = ['car', 'cart', 'cartoon']
    assert find_longest_common_prefix_reduce(words) == 'car'