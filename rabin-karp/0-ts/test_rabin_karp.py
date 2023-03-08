import pytest
from rabin_karp_substring_search import rabin_karp_find_substring

def test_rabin_karp():
    assert rabin_karp_find_substring('hello','llo') == 2
    assert rabin_karp_find_substring('aabbababaa','babaa') == 5

def test_rabin_karp_miss():
    assert rabin_karp_find_substring('hello','af') == -1

def test_find_first_with_mult():
    assert rabin_karp_find_substring('abcabbabcabb', 'abb') == 3

def test_same_hash_diff_order():
    assert rabin_karp_find_substring('Where are your ears?', 'ear', base=0) == 15
