import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

import pytest

def test_rabin_karp_find_substring():
    # Test when substring is found in the string
    assert rabin_karp_find_substring("hello world", "world") == 6
    assert rabin_karp_find_substring("abcdefg", "cde") == 2

def test_rabin_karp_find_substring_no_match():
    # Test when substring is not found in the string
    assert rabin_karp_find_substring("hello world", "abc") == -1
    assert rabin_karp_find_substring("abcdefg", "xyz") == -1

def test_rabin_karp_find_substring_edge_cases():
    # Test edge cases
    assert rabin_karp_find_substring("", "") == 0
    assert rabin_karp_find_substring("abcdefg", "abcdefg") == 0