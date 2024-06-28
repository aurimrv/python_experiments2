import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring('hello', 'll') == 2
    assert rabin_karp_find_substring('hello', 'hello') == 0
    assert rabin_karp_find_substring('hello', 'o') == 4

def test_rabin_karp_find_substring_edge_cases():
    assert rabin_karp_find_substring('abcdef', 'xyz') == -1
    assert rabin_karp_find_substring('aaa', 'a') == 0
    assert rabin_karp_find_substring('aaaaa', 'aa') == 0