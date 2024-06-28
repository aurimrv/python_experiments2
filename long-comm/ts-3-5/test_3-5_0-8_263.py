import os
import sys
from functools import reduce
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Test cases for find_longest_common_prefix function
def test_find_longest_common_prefix_empty_list():
    assert find_longest_common_prefix([]) == ''

def test_find_longest_common_prefix_single_word():
    assert find_longest_common_prefix(['apple']) == 'apple'

def test_find_longest_common_prefix_all_words_same():
    assert find_longest_common_prefix(['apple', 'apple', 'apple']) == 'apple'

def test_find_longest_common_prefix_general_case():
    assert find_longest_common_prefix(['apple', 'app', 'april']) == 'ap'

# Test cases for find_longest_common_prefix_reduce function
def test_find_longest_common_prefix_reduce_empty_list():
    assert find_longest_common_prefix_reduce([]) == ''

def test_find_longest_common_prefix_reduce_single_word():
    assert find_longest_common_prefix_reduce(['apple']) == 'apple'

def test_find_longest_common_prefix_reduce_all_words_same():
    assert find_longest_common_prefix_reduce(['apple', 'apple', 'apple']) == 'apple'

def test_find_longest_common_prefix_reduce_general_case():
    assert find_longest_common_prefix_reduce(['apple', 'app', 'april']) == 'ap'