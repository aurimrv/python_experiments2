import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    string = "hello world"
    substring = "world"
    assert rabin_karp_find_substring(string, substring) == 6

    string = "abcdeabcdeabcde"
    substring = "cde"
    assert rabin_karp_find_substring(string, substring) == 2

def test_rabin_karp_find_substring_edge_cases():
    string = "aaaaa"
    substring = "aaaaa"
    assert rabin_karp_find_substring(string, substring) == 0

    string = "abcdefg"
    substring = "xyz"
    assert rabin_karp_find_substring(string, substring) == -1

def test_rabin_karp_find_substring_primes():
    string = "ababab"
    substring = "aba"
    assert rabin_karp_find_substring(string, substring) == 0

    string = "mississippi"
    substring = "issi"
    assert rabin_karp_find_substring(string, substring) == 1