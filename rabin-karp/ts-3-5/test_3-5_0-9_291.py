import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test when substring is found in string
    assert rabin_karp_find_substring("hello world", "world") == 6
    assert rabin_karp_find_substring("abcdefg", "cde") == 2

    # Test when substring is not found in string
    assert rabin_karp_find_substring("hello", "world") == -1
    assert rabin_karp_find_substring("abcdefg", "xyz") == -1

    # Test when substring is at the beginning of the string
    assert rabin_karp_find_substring("hello", "hel") == 0
    assert rabin_karp_find_substring("abcdefg", "abc") == 0

    # Test when substring is at the end of the string
    assert rabin_karp_find_substring("hello", "lo") == 3
    assert rabin_karp_find_substring("abcdefg", "fg") == 5

    # Test with prime_modulus as input
    assert rabin_karp_find_substring("hello", "lo", prime_modulus=17) == 3
    assert rabin_karp_find_substring("hello", "lo", prime_modulus=31) == 3