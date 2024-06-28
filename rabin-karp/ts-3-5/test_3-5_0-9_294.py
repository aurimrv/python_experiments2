import os
import sys
import pytest

# Add the project directory to the sys path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring_single_match():
    string = "this is a test string for testing"
    substring = "test"
    assert rabin_karp_find_substring(string, substring) == 10

def test_rabin_karp_find_substring_multiple_matches():
    string = "ababababab"
    substring = "aba"
    assert rabin_karp_find_substring(string, substring) == 0

def test_rabin_karp_find_substring_no_match():
    string = "abcdefg"
    substring = "xyz"
    assert rabin_karp_find_substring(string, substring) == -1

def test_rabin_karp_find_substring_empty_strings():
    string = ""
    substring = ""
    assert rabin_karp_find_substring(string, substring) == 0

def test_rabin_karp_find_substring_long_string():
    string = "a" * 10**6
    substring = "a" * 10**4
    assert rabin_karp_find_substring(string, substring) == 0