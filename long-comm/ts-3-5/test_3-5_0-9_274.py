import os
import sys
from functools import reduce

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    words = ["apple", "application", "applesauce"]
    assert find_longest_common_prefix(words) == "appl"

    words = ["flower", "flow", "flight"]
    assert find_longest_common_prefix(words) == "fl"

    words = ["dog", "cat", "bird"]
    assert find_longest_common_prefix(words) == ""
    
def test_find_longest_common_prefix_reduce():
    words = ["apple", "application", "applesauce"]
    assert find_longest_common_prefix_reduce(words) == "appl"

    words = ["flower", "flow", "flight"]
    assert find_longest_common_prefix_reduce(words) == "fl"

    words = ["dog", "cat", "bird"]
    assert find_longest_common_prefix_reduce(words) == ""