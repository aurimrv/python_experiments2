import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test case for finding substring in a string
    assert rabin_karp_find_substring('hello', 'll') == 2

    # Test case for substring not found
    assert rabin_karp_find_substring('abcdef', 'xyz') == -1

def test_rabin_karp_find_substring_edge_cases():
    # Test case for empty string and empty substring
    assert rabin_karp_find_substring('', '') == 0

    # Test case for substring as the entire string
    assert rabin_karp_find_substring('testing', 'testing') == 0

    # Test case for substring at the beginning of the string
    assert rabin_karp_find_substring('abcdef', 'abc') == 0

    # Test case for substring at the end of the string
    assert rabin_karp_find_substring('abcdef', 'def') == 3

    # Test case for substring in the middle of the string
    assert rabin_karp_find_substring('abracadabra', 'cad') == 4