import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring("hello world", "world") == 6
    assert rabin_karp_find_substring("hello world", "hello") == 0

def test_rabin_karp_find_substring_empty_string():
    assert rabin_karp_find_substring("", "") == 0

def test_rabin_karp_find_substring_not_found():
    assert rabin_karp_find_substring("abcde", "fgh") == -1

def test_rabin_karp_find_substring_long_string():
    assert rabin_karp_find_substring("a" * 1000 + "bcd", "bcd") == 1000

def test_rabin_karp_find_substring_same_string():
    assert rabin_karp_find_substring("python", "python") == 0
    assert rabin_karp_find_substring("a" * 100, "a" * 100) == 0