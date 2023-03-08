import pytest
from permutations import permutations_of_word

def test_permutation_word():
    assert permutations_of_word('two') == ['two', 'tow', 'wto', 'wot', 'otw', 'owt']
    assert permutations_of_word('123') == ['123', '132', '213', '231', '312', '321']
