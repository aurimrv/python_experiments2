import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test cases for rabin_karp_find_substring method

    # Test case 1: Substring found in the string
    assert rabin_karp_find_substring("hello world", "world") == 6

    # Test case 2: Substring not found in the string
    assert rabin_karp_find_substring("hello world", "python") == -1

    # Test case 3: Substring found at the beginning of the string
    assert rabin_karp_find_substring("hello world", "hello") == 0

    # Test case 4: Substring found at the end of the string
    assert rabin_karp_find_substring("hello world", "world") == 6

    # Test case 5: Substring found multiple times in the string
    assert rabin_karp_find_substring("hellohellohello", "hello") == 0
    assert rabin_karp_find_substring("hellohellohello", "hello", base=10, prime_modulus=13) == 0