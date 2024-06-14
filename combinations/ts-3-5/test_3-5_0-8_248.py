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

    # Test case for a single character input
    assert combinations_of_word('a') == ['a']

    # Test case for a word with distinct characters
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']

    # Test case for a word with repeated characters
    assert combinations_of_word('aab') == ['a', 'aa', 'aab', 'a', 'ab', 'b']

def test_combinations_of_phone_input():
    # Test case for single digit input
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test case for input with duplicate digits
    assert combinations_of_phone_input('22') == ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

    # Test case for input with different digits
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test case for input with multiple digits
    assert combinations_of_phone_input('234') == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 
                                                   'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi',
                                                   'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
