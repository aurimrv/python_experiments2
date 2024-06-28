import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring("hello world", "world") == 6
    assert rabin_karp_find_substring("abracadabra", "cad") == 4
    assert rabin_karp_find_substring("aaaaaaa", "aaa") == 0
    assert rabin_karp_find_substring("testing", "z") == -1
    assert rabin_karp_find_substring("hello", "world") == -1
    assert rabin_karp_find_substring("", "") == 0

def test_rabin_karp_find_substring_edge_cases():
    assert rabin_karp_find_substring("abcdefghijklmnopqrstuvwxyz", "xyz") == 23
    assert rabin_karp_find_substring("aaaaaa", "a") == 0
    assert rabin_karp_find_substring("aaaaaa", "aa") == 0
    assert rabin_karp_find_substring("aaaaaa", "aaa") == 0
    assert rabin_karp_find_substring("aaaaaa", "aaa") == 0