import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    # Test when all words have the same prefix
    words = ["apple", "appletree", "append", "applause"]
    assert find_longest_common_prefix(words) == "app"

    # Test when there is no common prefix
    words = ["dog", "cat", "bird"]
    assert find_longest_common_prefix(words) == ""

def test_find_longest_common_prefix_reduce():
    # Test when all words have the same prefix
    words = ["apple", "appletree", "append", "applause"]
    assert find_longest_common_prefix_reduce(words) == "app"

    # Test when there is no common prefix
    words = ["dog", "cat", "bird"]
    assert find_longest_common_prefix_reduce(words) == ""

    # Test when one word is a prefix of the others
    words = ["car", "carrot", "carriage"]
    assert find_longest_common_prefix_reduce(words) == "car"

    # Test when one word is empty
    words = ["", "apple", "banana"]
    assert find_longest_common_prefix_reduce(words) == ""

    # Test when all words are empty
    words = ["", "", ""]
    assert find_longest_common_prefix_reduce(words) == ""

    # Test when words have no common prefix until the end
    words = ["apple", "banana", "orange"]
    assert find_longest_common_prefix_reduce(words) == ""

    # Test when words have common prefix until a certain point
    words = ["apple", "appletree", "applesauce"]
    assert find_longest_common_prefix_reduce(words) == "apple"