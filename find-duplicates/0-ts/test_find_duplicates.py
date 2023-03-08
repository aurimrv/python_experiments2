import pytest
from find_duplicates import duplicates_linear, duplicates_pre_sorted, duplicates_bin_search

def test_linear():
    assert duplicates_linear([1,2,3,4,5,6],[1,2,3,7,8,9]) == [1,2,3]
    assert duplicates_linear([4,5,7,1,9,2,10,3],[4,90,23,1,53,3,2,22]) == [4,1,3,2]

def test_pre_sorted():
    assert duplicates_pre_sorted([1,2,3,4,5,6],[1,2,3,7,8,9]) == [1,2,3]
    assert duplicates_pre_sorted([5,7,1,9,2,10,3],[4,90,23,1,53,3,2,22]) != [1,2,3]

def test_bin_search():
    assert duplicates_bin_search([1,2,3,4,5,6],[1,2,3,7,8,9]) == [1,2,3]
    assert duplicates_bin_search([1,2,3,4,5,6],[1,2,3,7,8,9,10,11,12,13,14,15]) == [1,2,3]

def test_bin_search_second_shorter():
    assert duplicates_bin_search([1,2,3,7,8,9,10,11,12,13,14,15],[1,2,3,4,5,6]) == [1,2,3]

