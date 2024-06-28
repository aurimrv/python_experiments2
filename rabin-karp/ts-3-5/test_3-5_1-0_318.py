import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import rabin_karp_substring_search

def test_rabin_karp_find_substring():
    # Test for substring present at the beginning
    assert rabin_karp_substring_search.rabin_karp_find_substring("hello", "he") == 0
    assert rabin_karp_substring_search.rabin_karp_find_substring("hello", "hell") == 0
    
    # Test for substring present at the end
    assert rabin_karp_substring_search.rabin_karp_find_substring("hello", "lo") == 3
    assert rabin_karp_substring_search.rabin_karp_find_substring("hello", "ello") == 1
    
    # Test for substring present multiple times
    assert rabin_karp_substring_search.rabin_karp_find_substring("ababab", "ab") == 0
    assert rabin_karp_substring_search.rabin_karp_find_substring("ababab", "ba") == 1
    
    # Test for substring not found
    assert rabin_karp_substring_search.rabin_karp_find_substring("abcde", "xy") == -1
    assert rabin_karp_substring_search.rabin_karp_find_substring("abcde", "dear") == -1