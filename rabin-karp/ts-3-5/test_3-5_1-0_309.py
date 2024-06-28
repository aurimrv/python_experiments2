import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring("hello", "ll") == 2
    assert rabin_karp_find_substring("hello", "world") == -1
    assert rabin_karp_find_substring("hellohello", "hello") == 0
    assert rabin_karp_find_substring("abcde", "c") == 2
    assert rabin_karp_find_substring("aaaaaa", "aaa") == 0
    assert rabin_karp_find_substring("banana", "nana") == 2
    assert rabin_karp_find_substring("mississippi", "ipp") == 7