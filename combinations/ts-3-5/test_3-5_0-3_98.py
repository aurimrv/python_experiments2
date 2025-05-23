import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test case for empty string
    assert combinations_of_word('') == []

    # Test case for single character string
    assert combinations_of_word('a') == ['a']

    # Test case for a simple word
    assert combinations_of_word('cat') == ['c', 'ca', 'cat', 'a', 'at', 't']

def test_combinations_of_phone_input():
    # Test case for single digit input
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test case for two-digit input
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test case for three-digit input
    assert combinations_of_phone_input('234') == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']

    # Test case for a single digit with multiple letters
    assert combinations_of_phone_input('9') == ['w', 'x', 'y', 'z']

    # Test case for a mix of digits and letters
    assert combinations_of_phone_input('239') == ['adw', 'adx', 'ady', 'adz', 'aew', 'aex', 'aey', 'aez', 'afw', 'afx', 'afy', 'afz', 'bdw', 'bdx', 'bdy', 'bdz', 'bew', 'bex', 'bey', 'bez', 'bfw', 'bfx', 'bfy', 'bfz', 'cdw', 'cdx', 'cdy', 'cdz', 'cew', 'cex', 'cey', 'cez', 'cfw', 'cfx', 'cfy', 'cfz']
