import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import combinations

def test_combinations_of_word():
    assert combinations.combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert combinations.combinations_of_word('123') == ['1', '12', '123', '2', '23', '3']
    assert combinations.combinations_of_word('xyz') == ['x', 'xy', 'xyz', 'y', 'yz', 'z']

def test_combinations_of_phone_input():
    assert combinations.combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert combinations.combinations_of_phone_input('9') == ['w', 'x', 'y', 'z']
    assert combinations.combinations_of_phone_input('72') == ['pa', 'pb', 'pc', 'qa', 'qb', 'qc', 'ra', 'rb', 'rc', 'sa', 'sb', 'sc']
