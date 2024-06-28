import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test when substring is found at the beginning of the string
    assert rabin_karp_find_substring("hello", "he") == 0

    # Test when substring is found in the middle of the string
    assert rabin_karp_find_substring("hello", "ell") == 1

    # Test when substring is found at the end of the string
    assert rabin_karp_find_substring("hello", "lo") == 3

    # Test when substring is not found in the string
    assert rabin_karp_find_substring("hello", "abc") == -1

    # Test with prime_modulus as a different prime number
    assert rabin_karp_find_substring("hello", "lo", prime_modulus=491) == 3

    # Test with base as a different value
    assert rabin_karp_find_substring("hello", "el", base=10) == 1