import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix_empty_input():
    assert find_longest_common_prefix([]) == ""

def test_find_longest_common_prefix_single_word():
    assert find_longest_common_prefix(["apple"]) == "apple"

def test_find_longest_common_prefix_no_common_prefix():
    assert find_longest_common_prefix(["dog", "car", "hat"]) == ""

def test_find_longest_common_prefix_common_prefix():
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_find_longest_common_prefix_reduce_empty_input():
    assert find_longest_common_prefix_reduce([]) == ""

def test_find_longest_common_prefix_reduce_single_word():
    assert find_longest_common_prefix_reduce(["python"]) == "python"

def test_find_longest_common_prefix_reduce_no_common_prefix():
    assert find_longest_common_prefix_reduce(["house", "boat", "tree"]) == ""

def test_find_longest_common_prefix_reduce_common_prefix():
    assert find_longest_common_prefix_reduce(["music", "musical", "musicians"]) == "music"