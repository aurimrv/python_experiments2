import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test when substring is found at the beginning of the string
    assert rabin_karp_find_substring("hello world", "hello") == 0

    # Test when substring is found in the middle of the string
    assert rabin_karp_find_substring("hello world", "world") == 6

    # Test when substring is found at the end of the string
    assert rabin_karp_find_substring("hello world", "world") == 6

    # Test when substring is not found in the string
    assert rabin_karp_find_substring("hello world", "python") == -1

    # Test with custom base and prime modulus
    assert rabin_karp_find_substring("hello world", "world", base=10, prime_modulus=17) == 6