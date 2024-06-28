import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring("hello", "ll") == 2
    assert rabin_karp_find_substring("hello", "lo") == 3

def test_rabin_karp_find_substring_edge_cases():
    assert rabin_karp_find_substring("hello", "h") == 0
    assert rabin_karp_find_substring("hello", "hello") == 0
    assert rabin_karp_find_substring("hello", "z") == -1
    assert rabin_karp_find_substring("hello", "ell") == 1

def test_rabin_karp_find_substring_custom_prime_modulus():
    assert rabin_karp_find_substring("hello", "lo", prime_modulus=17) == 3
    assert rabin_karp_find_substring("hello", "he", prime_modulus=13) == 0