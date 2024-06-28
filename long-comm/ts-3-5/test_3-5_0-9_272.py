import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_find_longest_common_prefix():
    # Test empty list
    words = []
    assert find_longest_common_prefix(words) == ""
    
    # Test single word in list
    words = ["apple"]
    assert find_longest_common_prefix(words) == "apple"
    
    # Test words with different prefixes
    words = ["apple", "banana", "cherry"]
    assert find_longest_common_prefix(words) == ""
    
    # Test words with common prefix
    words = ["apple", "application", "appetizer"]
    assert find_longest_common_prefix(words) == "app"

def test_find_longest_common_prefix_reduce():
    # Test empty list
    words = []
    assert find_longest_common_prefix_reduce(words) == ""
    
    # Test single word in list
    words = ["apple"]
    assert find_longest_common_prefix_reduce(words) == "apple"
    
    # Test words with different prefixes
    words = ["apple", "banana", "cherry"]
    assert find_longest_common_prefix_reduce(words) == ""
    
    # Test words with common prefix
    words = ["apple", "application", "appetizer"]
    assert find_longest_common_prefix_reduce(words) == "app"