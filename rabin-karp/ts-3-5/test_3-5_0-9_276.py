import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

# Test cases for rabin_karp_find_substring

def test_rabin_karp_find_substring_exact_match():
    assert rabin_karp_find_substring('hello', 'lo') == 3
    
def test_rabin_karp_find_substring_no_match():
    assert rabin_karp_find_substring('hello', 'world') == -1

def test_rabin_karp_find_substring_partial_match():
    assert rabin_karp_find_substring('hello', 'ell') == 1

def test_rabin_karp_find_substring_repeated_substr():
    assert rabin_karp_find_substring('ababab', 'ab') == 0

def test_rabin_karp_find_substring_long_strings():
    assert rabin_karp_find_substring('This is a test string', 'test') == 10