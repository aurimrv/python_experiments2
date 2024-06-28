import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    assert rabin_karp_find_substring("hello", "hel") == 0
    assert rabin_karp_find_substring("hello", "h") == 0
    assert rabin_karp_find_substring("hello", "ell") == 1
    assert rabin_karp_find_substring("hello", "ell") == 1
    assert rabin_karp_find_substring("hello", "lo") == 3
    assert rabin_karp_find_substring("hello", "o") == 4
    assert rabin_karp_find_substring("hello", "abc") == -1
    assert rabin_karp_find_substring("hello", "xyz") == -1
    assert rabin_karp_find_substring("This is a long string", "long") == 10
    assert rabin_karp_find_substring("Also a long string", "long") == 7