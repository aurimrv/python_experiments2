import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test when input is an empty string
    assert combinations_of_word('') == []

    # Test when input is a single letter
    assert combinations_of_word('a') == ['a']

    # Test when input is a two-letter word
    assert combinations_of_word('ab') == ['a', 'ab', 'b']

    # Test when input is a three-letter word
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']

def test_combinations_of_phone_input():
    # Test when input is a single digit
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test when input is '23'
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test when input is '456'
    assert combinations_of_phone_input('456') == ['gjm', 'gjn', 'gjo', 'gkm', 'gkn', 'gko', 'glm', 'gln', 'glo', 'hjm', 'hjn', 'hjo', 'hkm', 'hkn', 'hko', 'hlm', 'hln', 'hlo', 'ijm', 'ijn', 'ijo', 'ikm', 'ikn', 'iko', 'ilm', 'iln', 'ilo']