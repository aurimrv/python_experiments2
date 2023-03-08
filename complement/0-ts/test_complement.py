import pytest
from complement import complement

def test_complement():
    assert complement(0b101) == 0b010
    assert complement(0b10) == 0b01
    assert complement(0b1100111010111110000) == 0b0011000101000001111
    assert complement(0b0) == 0b1

