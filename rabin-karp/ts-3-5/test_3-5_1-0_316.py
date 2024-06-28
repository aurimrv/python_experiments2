import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

# Test cases for rabin_karp_find_substring method
def test_rabin_karp_find_substring_no_match():
    string = "abcd"
    substring = "xyz"
    assert rabin_karp_find_substring(string, substring) == -1

def test_rabin_karp_find_substring_single_match():
    string = "hello world"
    substring = "world"
    assert rabin_karp_find_substring(string, substring) == 6

def test_rabin_karp_find_substring_multiple_matches():
    string = "aaaaaa"
    substring = "aa"
    assert rabin_karp_find_substring(string, substring) == 0

def test_rabin_karp_find_substring_different_base():
    string = "ABCDE"
    substring = "CDE"
    assert rabin_karp_find_substring(string, substring, base=10) == 2

def test_rabin_karp_find_substring_large_prime_modulus():
    string = "AAABBBCCC"
    substring = "BBB"
    assert rabin_karp_find_substring(string, substring, prime_modulus=997) == 3