import pytest
from longest_common_prefix import find_longest_common_prefix, find_longest_common_prefix_reduce

def test_lcp():
    assert find_longest_common_prefix(['hello', 'hellieo', 'he']) == 'he'
    assert find_longest_common_prefix_reduce(['hello', 'hellieo', 'he']) == 'he'

def test_lcp_empty():
    assert find_longest_common_prefix([]) == ''
    assert find_longest_common_prefix_reduce([]) == ''

def test_lcp_no_prefix():
    assert find_longest_common_prefix(['fcp', 'jpl', 'the', 'first']) == ''
    assert find_longest_common_prefix_reduce(['fcp', 'jpl', 'the', 'first']) == ''

def test_lcp_full_prefix():
    assert find_longest_common_prefix(['full', 'full', 'full']) == 'full'
    assert find_longest_common_prefix_reduce(['full', 'full', 'full']) == 'full'

