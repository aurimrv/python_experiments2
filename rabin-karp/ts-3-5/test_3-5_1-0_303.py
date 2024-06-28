import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring("hello world", "world") == 6
    assert rabin_karp_find_substring("hello world", "hello") == 0
    assert rabin_karp_find_substring("mississippi", "issi") == 1
    assert rabin_karp_find_substring("abracadabra", "cad") == 4

def test_rabin_karp_find_substring_edge_cases():
    assert rabin_karp_find_substring("abc", "def") == -1
    assert rabin_karp_find_substring("test", "test") == 0
    assert rabin_karp_find_substring("aaaaaaa", "aa") == 0