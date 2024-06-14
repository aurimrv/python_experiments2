import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test for input 'abc'
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']
    
    # Test for input 'dog'
    assert combinations_of_word('dog') == ['d', 'do', 'dog', 'o', 'og', 'g']

def test_combinations_of_phone_input():
    # Test for input '23'
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test for input '78'
    assert combinations_of_phone_input('78') == ['pt', 'pu', 'pv', 'qt', 'qu', 'qv', 'rt', 'ru', 'rv', 'st', 'su', 'sv']
