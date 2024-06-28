import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test when substring is found in the string
    assert rabin_karp_find_substring("hello world", "world") == 6
    assert rabin_karp_find_substring("hello world", "hello") == 0

    # Test when substring is not found in the string
    assert rabin_karp_find_substring("hello world", "python") == -1
    assert rabin_karp_find_substring("hello world", "hi") == -1

    # Test with empty string
    assert rabin_karp_find_substring("", "") == 0

    # Test with empty substring
    assert rabin_karp_find_substring("hello world", "") == 0

    # Test with repeated substring
    assert rabin_karp_find_substring("abababab", "ab") == 0
    assert rabin_karp_find_substring("abababab", "ba") == 1