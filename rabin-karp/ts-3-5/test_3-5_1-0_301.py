import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test case where substring is at the beginning of the string
    assert rabin_karp_find_substring("hello", "he") == 0

    # Test case where substring is at the end of the string
    assert rabin_karp_find_substring("hello", "lo") == 3

    # Test case where substring is in the middle of the string
    assert rabin_karp_find_substring("hello", "ell") == 1

    # Test case where substring is not found in the string
    assert rabin_karp_find_substring("hello", "abc") == -1

def test_rabin_karp_find_substring_multiple_occurrences():
    # Test case where substring occurs multiple times in the string
    assert rabin_karp_find_substring("ababab", "ab") == 0

    # Test case where substring occurs multiple times and not at the beginning
    assert rabin_karp_find_substring("ababab", "ba") == 1

    # Test case where substring occurs multiple times and not at the end
    assert rabin_karp_find_substring("ababab", "ab") == 0

    # Test case where substring occurs multiple times and overlaps
    assert rabin_karp_find_substring("aaa", "aa") == 0