import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring_exact_match():
    string = "hello world"
    substring = "world"
    assert rabin_karp_find_substring(string, substring) == 6

def test_rabin_karp_find_substring_no_match():
    string = "hello world"
    substring = "test"
    assert rabin_karp_find_substring(string, substring) == -1

def test_rabin_karp_find_substring_partial_match():
    string = "hello hello world"
    substring = "world"
    assert rabin_karp_find_substring(string, substring) == 12

def test_rabin_karp_find_substring_base_prime():
    string = "hello world"
    substring = "hello"
    assert rabin_karp_find_substring(string, substring, base=257, prime_modulus=491) == 0