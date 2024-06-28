import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    # Test case 1: Empty list of words
    assert find_longest_common_prefix([]) == ''

    # Test case 2: List of words with no common prefix
    assert find_longest_common_prefix(['apple', 'banana', 'cherry']) == ''

    # Test case 3: List of words with common prefix
    assert find_longest_common_prefix(['flow', 'flower', 'flight']) == 'fl'

def test_find_longest_common_prefix_reduce():
    # Test case 1: Empty list of words
    assert find_longest_common_prefix_reduce([]) == ''

    # Test case 2: List of words with no common prefix
    assert find_longest_common_prefix_reduce(['apple', 'banana', 'cherry']) == ''

    # Test case 3: List of words with common prefix
    assert find_longest_common_prefix_reduce(['flow', 'flower', 'flight']) == 'fl'