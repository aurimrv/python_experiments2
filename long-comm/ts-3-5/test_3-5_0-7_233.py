import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    words = ['apple', 'app', 'april']
    assert find_longest_common_prefix(words) == 'ap'
    words = ['flower', 'flow', 'flight']
    assert find_longest_common_prefix(words) == 'fl'
    words = ['dog', 'racecar', 'car']
    assert find_longest_common_prefix(words) == ''
    words = ['dog', 'dog', 'dog']
    assert find_longest_common_prefix(words) == 'dog'

def test_find_longest_common_prefix_reduce():
    words = ['apple', 'app', 'april']
    assert find_longest_common_prefix_reduce(words) == 'ap'
    words = ['flower', 'flow', 'flight']
    assert find_longest_common_prefix_reduce(words) == 'fl'
    words = ['dog', 'racecar', 'car']
    assert find_longest_common_prefix_reduce(words) == ''
    words = ['dog', 'dog', 'dog']
    assert find_longest_common_prefix_reduce(words) == 'dog'