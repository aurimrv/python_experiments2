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
    
    # Test case for single letter
    assert combinations_of_word('a') == ['a']
    
    # Test case for word with 3 unique letters
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']

def test_combinations_of_phone_input():
    # Test case for single number input
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']
    
    # Test case for numbers '234'
    expected_output = ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi',
                       'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi',
                       'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
    assert combinations_of_phone_input('234') == expected_output
    
    # Test case for numbers '79'
    expected_output = ['pw', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz', 
                       'rw', 'rx', 'ry', 'rz', 'sw', 'sx', 'sy', 'sz']
    assert combinations_of_phone_input('79') == expected_output