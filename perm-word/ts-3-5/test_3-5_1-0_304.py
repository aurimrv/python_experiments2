import sys
import os
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from permutations import permutations_of_word

def test_empty_string():
    string = ""
    assert permutations_of_word(string) == ['']

def test_single_character():
    string = "a"
    assert permutations_of_word(string) == ['a']

def test_two_characters():
    string = "ab"
    assert set(permutations_of_word(string)) == set(['ab', 'ba'])

def test_three_characters():
    string = "abc"
    assert set(permutations_of_word(string)) == set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

def test_same_characters():
    string = "aaa"
    assert set(permutations_of_word(string)) == set(['aaa'])

def test_four_characters():
    string = "abcd"
    assert set(permutations_of_word(string)) == set(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 
                                                       'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 
                                                       'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 
                                                       'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])