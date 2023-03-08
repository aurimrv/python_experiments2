import pytest
from first_missing_positive import first_missing_positive

def test_in_order():
    assert first_missing_positive([1,2,3,4,5]) == 6
    assert first_missing_positive([0,1,2,3,4,5]) == 6

def test_with_negatives():
    assert first_missing_positive([-1,0,-3,6,-5,2,5,3,4,-9,0,1]) == 7

def test_filled_with_zeros():
    assert first_missing_positive([0,0,0,1,0,0,0,0,0,2,0,0,0,0]) == 3

