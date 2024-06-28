import pytest
import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from permutations import permutations_of_word

def test_permutations_of_word_empty_string():
    assert permutations_of_word('') == ['']

def test_permutations_of_word_single_letter():
    assert permutations_of_word('a') == ['a']

def test_permutations_of_word_multiple_letters():
    assert set(permutations_of_word('abc')) == set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

def test_permutations_of_word_repeated_letters():
    assert set(permutations_of_word('aab')) == set(['aab', 'aba', 'baa'])

def test_permutations_of_word_special_characters():
    assert permutations_of_word('!@#') == ['!@#', '!#@', '@!#', '@#!', '#!@', '#@!']