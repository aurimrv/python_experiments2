import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test case for finding exact match
    assert rabin_karp_find_substring('hello', 'ell') == 1

    # Test case for finding match at the beginning of the string
    assert rabin_karp_find_substring('hello', 'hel') == 0

    # Test case for finding match at the end of the string
    assert rabin_karp_find_substring('hello', 'llo') == 2

    # Test case for substring not found
    assert rabin_karp_find_substring('hello', 'abc') == -1

    # Test case for using a different prime modulus
    assert rabin_karp_find_substring('hello', 'lo', prime_modulus=11) == 3