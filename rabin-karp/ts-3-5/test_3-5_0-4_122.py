import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test case where substring is found in the string
    assert rabin_karp_find_substring("hello", "ell") == 1
    assert rabin_karp_find_substring("abcdefg", "bcd") == 1

    # Test case where substring is not found in the string
    assert rabin_karp_find_substring("hello", "world") == -1
    assert rabin_karp_find_substring("abcdefg", "xyz") == -1

    # Test case where substring is at the beginning of the string
    assert rabin_karp_find_substring("hello", "hel") == 0
    assert rabin_karp_find_substring("abcdefg", "abc") == 0

    # Test case where substring is at the end of the string
    assert rabin_karp_find_substring("hello", "lo") == 3
    assert rabin_karp_find_substring("abcdefg", "efg") == 4

    # Test case where substring is empty
    assert rabin_karp_find_substring("hello", "") == 0
    assert rabin_karp_find_substring("abcdefg", "") == 0