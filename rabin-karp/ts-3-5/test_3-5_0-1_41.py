import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test when substring is found in the string
    assert rabin_karp_find_substring("hello", "ell") == 1
    assert rabin_karp_find_substring("hello", "hello") == 0

    # Test when substring is not found in the string
    assert rabin_karp_find_substring("hello", "world") == -1
    assert rabin_karp_find_substring("hello", "lorem") == -1

    # Test with different base and prime_modulus values
    assert rabin_karp_find_substring("hello", "lo", base=10, prime_modulus=17) == 3
    assert rabin_karp_find_substring("hello", "hello", base=2, prime_modulus=31) == 0