import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test for empty string
    assert combinations_of_word('') == []

    # Test for single character string
    assert combinations_of_word('a') == ['a']

    # Test for a string with multiple characters
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']

def test_combinations_of_phone_input():
    # Test for single digit input
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test for input with repeated digits
    assert combinations_of_phone_input('22') == ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

    # Test for input with different digits
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']