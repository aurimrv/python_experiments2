import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert combinations_of_word('dog') == ['d', 'do', 'dog', 'o', 'og', 'g']
    assert combinations_of_word('123') == ['1', '12', '123', '2', '23', '3']

def test_combinations_of_phone_input():
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert combinations_of_phone_input('47') == ['gp', 'gq', 'gr', 'gs', 'hp', 'hq', 'hr', 'hs', 'ip', 'iq', 'ir', 'is']
    assert combinations_of_phone_input('9') == ['w', 'x', 'y', 'z']