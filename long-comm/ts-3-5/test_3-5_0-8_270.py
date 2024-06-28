import os
import sys
from functools import reduce

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    words = ['apple', 'apricot', 'application']
    assert find_longest_common_prefix(words) == 'ap'

    words = ['dog', 'cat', 'mouse']
    assert find_longest_common_prefix(words) == ''

    words = ['car', 'carrot', 'carriage']
    assert find_longest_common_prefix(words) == 'car'

def test_find_longest_common_prefix_reduce():
    words = ['apple', 'apricot', 'application']
    assert find_longest_common_prefix_reduce(words) == 'ap'

    words = ['dog', 'cat', 'mouse']
    assert find_longest_common_prefix_reduce(words) == ''

    words = ['car', 'carrot', 'carriage']
    assert find_longest_common_prefix_reduce(words) == 'car'