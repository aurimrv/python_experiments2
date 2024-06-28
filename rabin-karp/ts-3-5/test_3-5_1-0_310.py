import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring("hello", "ll") == 2

def test_rabin_karp_find_substring_with_base_and_prime_modulus():
    assert rabin_karp_find_substring("hello", "lo", 256, 487) == 3

def test_rabin_karp_find_substring_multiple_occurrences():
    assert rabin_karp_find_substring("abracadabra", "abra") == 0
    assert rabin_karp_find_substring("abracadabra", "bra") == 1

def test_rabin_karp_find_substring_no_occurrence():
    assert rabin_karp_find_substring("hello", "xyz") == -1

def test_rabin_karp_find_substring_long_substring():
    assert rabin_karp_find_substring("abcdef", "abcdef") == 0