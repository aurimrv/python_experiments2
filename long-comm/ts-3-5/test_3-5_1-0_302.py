import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Test cases for find_longest_common_prefix method
def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_one_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_common_prefix():
    words = ['apple', 'app', 'apply']
    assert find_longest_common_prefix(words) == 'app'

def test_find_longest_common_prefix_no_common_prefix():
    words = ['hello', 'world', 'python']
    assert find_longest_common_prefix(words) == ''

# Test cases for find_longest_common_prefix_reduce method
def test_find_longest_common_prefix_reduce_empty_list():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_one_word():
    words = ['apple']
    assert find_longest_common_prefix_reduce(words) == 'apple'

def test_find_longest_common_prefix_reduce_common_prefix():
    words = ['apple', 'app', 'apply']
    assert find_longest_common_prefix_reduce(words) == 'app'

def test_find_longest_common_prefix_reduce_no_common_prefix():
    words = ['hello', 'world', 'python']
    assert find_longest_common_prefix_reduce(words) == ''