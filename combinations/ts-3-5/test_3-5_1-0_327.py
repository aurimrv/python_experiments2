import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

# Test cases for combinations_of_word function
def test_combinations_of_word_empty_string():
    assert combinations_of_word("") == []

def test_combinations_of_word_single_letter():
    assert combinations_of_word("a") == ["a"]

def test_combinations_of_word_three_letters():
    assert combinations_of_word("abc") == ['a', 'ab', 'abc', 'b', 'bc', 'c']

# Test cases for combinations_of_phone_input function
def test_combinations_of_phone_input_single_digit():
    assert combinations_of_phone_input("2") == ['a', 'b', 'c']

def test_combinations_of_phone_input_two_digits():
    assert combinations_of_phone_input("23") == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

def test_combinations_of_phone_input_three_digits():
    assert combinations_of_phone_input("234") == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 
                                                  'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 
                                                  'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']