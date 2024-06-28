import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp_find_substring():
    # Test cases for rabin_karp_find_substring method

    # Test case 1: Valid substring in the string
    assert rabin_karp_find_substring('hello', 'll') == 2

    # Test case 2: Substring not found in the string
    assert rabin_karp_find_substring('hello', 'world') == -1

    # Test case 3: Substring at the beginning of the string
    assert rabin_karp_find_substring('hello', 'he') == 0

    # Test case 4: Substring at the end of the string
    assert rabin_karp_find_substring('hello', 'lo') == 3

    # Test case 5: Substring with special characters
    assert rabin_karp_find_substring('hello123', '123') == 5

    # Test case 6: Substring with numbers
    assert rabin_karp_find_substring('123hello', 'hello') == 3