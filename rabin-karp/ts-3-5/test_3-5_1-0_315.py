import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring_single_match():
    string = "hello"
    substring = "ll"
    assert rabin_karp_find_substring(string, substring) == 2

def test_rabin_karp_find_substring_multiple_matches():
    string = "ababab"
    substring = "ab"
    assert rabin_karp_find_substring(string, substring) == 0

def test_rabin_karp_find_substring_no_match():
    string = "abcdef"
    substring = "xyz"
    assert rabin_karp_find_substring(string, substring) == -1

def test_rabin_karp_find_substring_long_string():
    string = "abcdefghijklmnopqrstuvwxyz"
    substring = "xyz"
    assert rabin_karp_find_substring(string, substring) == 23