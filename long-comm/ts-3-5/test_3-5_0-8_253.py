import os
import sys
project_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert find_longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert find_longest_common_prefix([]) == ""

def test_find_longest_common_prefix_reduce():
    assert find_longest_common_prefix_reduce(["flower", "flow", "flight"]) == "fl"
    assert find_longest_common_prefix_reduce(["dog", "racecar", "car"]) == ""
    assert find_longest_common_prefix_reduce([]) == ""