import os
import sys
import pytest

# Importing the file and modules to be tested
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

# Test cases for find_longest_common_prefix method
def test_find_longest_common_prefix_empty_list():
    words = []
    assert find_longest_common_prefix(words) == ''

def test_find_longest_common_prefix_single_word():
    words = ['apple']
    assert find_longest_common_prefix(words) == 'apple'

def test_find_longest_common_prefix_same_words():
    words = ['dog', 'dog', 'dog']
    assert find_longest_common_prefix(words) == 'dog'

def test_find_longest_common_prefix_different_words():
    words = ['flower', 'flow', 'flight']
    assert find_longest_common_prefix(words) == 'fl'

# Test cases for find_longest_common_prefix_reduce method
def test_find_longest_common_prefix_reduce_empty_list():
    words = []
    assert find_longest_common_prefix_reduce(words) == ''

def test_find_longest_common_prefix_reduce_single_word():
    words = ['python']
    assert find_longest_common_prefix_reduce(words) == 'python'

def test_find_longest_common_prefix_reduce_same_words():
    words = ['cat', 'cat', 'cat']
    assert find_longest_common_prefix_reduce(words) == 'cat'

def test_find_longest_common_prefix_reduce_different_words():
    words = ['book', 'box', 'boy']
    assert find_longest_common_prefix_reduce(words) == 'bo'