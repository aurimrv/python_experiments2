import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test empty string
    assert combinations_of_word('') == []

    # Test single character string
    assert combinations_of_word('a') == ['a']

    # Test string with multiple characters
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']

def test_combinations_of_phone_input():
    # Test single digit input
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test input with multiple digits
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test input with repeating digits
    assert combinations_of_phone_input('222') == ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']