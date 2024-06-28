import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring("hello world", "world") == 6
    assert rabin_karp_find_substring("abcabcabc", "abc") == 0
    assert rabin_karp_find_substring("mississippi", "issi") == 1
    assert rabin_karp_find_substring("abcdef", "xyz") == -1

def test_rabin_karp_find_substring_hash_collision():
    assert rabin_karp_find_substring("aaaaaaa", "aaa") == 0
    assert rabin_karp_find_substring("ababababab", "aba") == 0
    assert rabin_karp_find_substring("abcde", "cde") == 2
    assert rabin_karp_find_substring("xyzxyz", "xyz") == 0

def test_rabin_karp_find_substring_boundary_cases():
    assert rabin_karp_find_substring("", "") == 0
    assert rabin_karp_find_substring("a", "a") == 0
    assert rabin_karp_find_substring("abcdef", "abcdef") == 0
    assert rabin_karp_find_substring("aaaa", "b") == -1