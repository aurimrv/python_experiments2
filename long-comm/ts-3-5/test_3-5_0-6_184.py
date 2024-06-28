import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    words = ["flower", "flow", "flight"]
    assert find_longest_common_prefix(words) == "fl"

    words = ["dog", "racecar", "car"]
    assert find_longest_common_prefix(words) == ""

    words = ["apple", "application", "appetizer"]
    assert find_longest_common_prefix(words) == "app"

def test_find_longest_common_prefix_reduce():
    words = ["flower", "flow", "flight"]
    assert find_longest_common_prefix_reduce(words) == "fl"

    words = ["dog", "racecar", "car"]
    assert find_longest_common_prefix_reduce(words) == ""

    words = ["apple", "application", "appetizer"]
    assert find_longest_common_prefix_reduce(words) == "app"