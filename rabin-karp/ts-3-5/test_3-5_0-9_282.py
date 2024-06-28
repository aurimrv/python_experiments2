import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test case when substring is found at the beginning of the string
    assert rabin_karp_find_substring("hello", "he") == 0

    # Test case when substring is found in the middle of the string
    assert rabin_karp_find_substring("hello", "ll") == 2

    # Test case when substring is found at the end of the string
    assert rabin_karp_find_substring("hello", "lo") == 3

    # Test case when substring is not found in the string
    assert rabin_karp_find_substring("hello", "world") == -1

    # Test case with prime_modulus being a large prime number
    assert rabin_karp_find_substring("abcde", "cde", prime_modulus=997) == 2

    # Test case with base being a custom value
    assert rabin_karp_find_substring("testing", "ing", base=10) == 4