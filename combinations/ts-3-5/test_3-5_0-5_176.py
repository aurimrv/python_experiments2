import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test 1: Empty string
    assert combinations_of_word('') == []

    # Test 2: Single character
    assert combinations_of_word('a') == ['a']

    # Test 3: Word with different characters
    assert combinations_of_word('cat') == ['c', 'ca', 'cat', 'a', 'at', 't']

def test_combinations_of_phone_input():
    # Test 1: Single digit
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test 2: Two different digits
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test 3: Repeating digits
    assert combinations_of_phone_input('22') == ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']