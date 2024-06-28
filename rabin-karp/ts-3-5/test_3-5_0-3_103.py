import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test when substring is found in the string
    assert rabin_karp_find_substring("hello", "ell") == 1
    assert rabin_karp_find_substring("abcde", "bcd") == 1

    # Test when substring is not found in the string
    assert rabin_karp_find_substring("hello", "abc") == -1
    assert rabin_karp_find_substring("abcde", "xyz") == -1

    # Test when substring is at the beginning of the string
    assert rabin_karp_find_substring("hello", "hel") == 0
    assert rabin_karp_find_substring("abcde", "abc") == 0

    # Test when substring is at the end of the string
    assert rabin_karp_find_substring("hello", "llo") == 2
    assert rabin_karp_find_substring("abcde", "cde") == 2

    # Test when substring is empty
    assert rabin_karp_find_substring("hello", "") == 0
    assert rabin_karp_find_substring("abcde", "") == 0