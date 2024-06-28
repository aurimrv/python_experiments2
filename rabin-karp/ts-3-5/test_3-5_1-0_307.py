import os
import sys
import pytest

# Adding the project directory to the sys path for correct imports
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

# Test cases for the rabin_karp_find_substring method
def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring("hello", "ll") == 2

def test_rabin_karp_find_substring_empty_string():
    assert rabin_karp_find_substring("", "") == 0

def test_rabin_karp_find_substring_no_match():
    assert rabin_karp_find_substring("python", "java") == -1

def test_rabin_karp_find_substring_full_match():
    assert rabin_karp_find_substring("art", "art") == 0

def test_rabin_karp_find_substring_multiple_occurrences():
    assert rabin_karp_find_substring("testtesttest", "test") == 0

def test_rabin_karp_find_substring_long_strings():
    assert rabin_karp_find_substring("longstringexample", "example") == 10