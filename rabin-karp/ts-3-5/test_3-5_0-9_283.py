import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Testing when substring is found in the string
    assert rabin_karp_find_substring("hello", "ell") == 1
    assert rabin_karp_find_substring("hello", "lo") == 3

    # Testing when substring is not found in the string
    assert rabin_karp_find_substring("hello", "abc") == -1
    assert rabin_karp_find_substring("hello", "world") == -1

    # Testing with different base and prime_modulus values
    assert rabin_karp_find_substring("hello", "lo", base=10, prime_modulus=101) == 3
    assert rabin_karp_find_substring("hello", "h", base=2, prime_modulus=17) == 0

    # Testing with empty string and substring
    assert rabin_karp_find_substring("", "") == 0
    assert rabin_karp_find_substring("hello", "") == 0

    # Testing repetitive substrings
    assert rabin_karp_find_substring("aaaa", "aa") == 0
    assert rabin_karp_find_substring("aaaa", "aaa") == 0