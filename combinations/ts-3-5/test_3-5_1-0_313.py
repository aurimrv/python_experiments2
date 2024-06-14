import os
import sys
import pytest
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
from combinations import combinations_of_word, combinations_of_phone_input

# Test cases for combinations_of_word
def test_combinations_of_word_empty_string():
    assert combinations_of_word("") == []

def test_combinations_of_word_single_letter():
    assert combinations_of_word("a") == ['a']

def test_combinations_of_word_short_string():
    assert combinations_of_word("ab") == ['a', 'ab', 'b']

def test_combinations_of_word_long_string():
    assert combinations_of_word("abcd") == ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']

# Test cases for combinations_of_phone_input
def test_combinations_of_phone_input_single_digit():
    assert combinations_of_phone_input("2") == ['a', 'b', 'c']

def test_combinations_of_phone_input_multiple_digits():
    assert combinations_of_phone_input("23") == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

def test_combinations_of_phone_input_long_input():
    assert combinations_of_phone_input("456") == ['gjm', 'gjn', 'gjo', 'gkm', 'gkn', 'gko', 'glm', 'gln', 'glo', 'hjm', 'hjn', 'hjo', 'hkm', 'hkn', 'hko', 'hlm', 'hln', 'hlo', 'ijm', 'ijn', 'ijo', 'ikm', 'ikn', 'iko', 'ilm', 'iln', 'ilo']

def test_combinations_of_phone_input_single_digit_long_output():
    assert combinations_of_phone_input("9") == ['w', 'x', 'y', 'z']
