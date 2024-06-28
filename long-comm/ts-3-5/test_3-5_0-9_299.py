import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    assert find_longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
    assert find_longest_common_prefix([]) == ''
    assert find_longest_common_prefix(['abc', 'def', 'ghi']) == ''
    assert find_longest_common_prefix(['apple', 'app', 'april']) == 'ap'
    assert find_longest_common_prefix(['abc', 'abcd', 'ab']) == 'ab'

def test_find_longest_common_prefix_reduce():
    assert find_longest_common_prefix_reduce(['flower', 'flow', 'flight']) == 'fl'
    assert find_longest_common_prefix_reduce([]) == ''
    assert find_longest_common_prefix_reduce(['abc', 'def', 'ghi']) == ''
    assert find_longest_common_prefix_reduce(['apple', 'app', 'april']) == 'ap'
    assert find_longest_common_prefix_reduce(['abc', 'abcd', 'ab']) == 'ab'