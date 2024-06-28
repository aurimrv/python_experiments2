import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test when substring is found in the string
    assert rabin_karp_find_substring("hello", "ell") == 1
    assert rabin_karp_find_substring("hello", "o") == 4
    assert rabin_karp_find_substring("hello", "h") == 0
    
    # Test when substring is not found in the string
    assert rabin_karp_find_substring("hello", "world") == -1
    assert rabin_karp_find_substring("hello", "hi") == -1
    assert rabin_karp_find_substring("hello", "z") == -1
    
    # Test when substring is empty
    assert rabin_karp_find_substring("hello", "") == 0
    assert rabin_karp_find_substring("", "") == 0

    # Test with different base and prime_modulus values
    assert rabin_karp_find_substring("hello", "ll", base=10, prime_modulus=13) == 2
    assert rabin_karp_find_substring("hello", "hello", base=2, prime_modulus=31) == 0