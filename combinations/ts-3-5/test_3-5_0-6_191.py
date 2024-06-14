import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test case 1: Empty string
    assert combinations_of_word('') == []
    
    # Test case 2: Single character
    assert combinations_of_word('a') == ['a']
    
    # Test case 3: Word with multiple characters
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']

def test_combinations_of_phone_input():
    # Test case 1: Phone input with single character
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']
    
    # Test case 2: Phone input with multiple characters
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    
    # Test case 3: Phone input with repeated characters
    assert combinations_of_phone_input('22') == ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']