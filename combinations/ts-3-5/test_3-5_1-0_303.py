import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Testing with input 'abc'
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']

    # Testing with input '1234'
    assert combinations_of_word('1234') == ['1', '12', '123', '1234', '2', '23', '234', '3', '34', '4']

def test_combinations_of_phone_input():
    # Testing with input '2'
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Testing with input '79'
    assert combinations_of_phone_input('79') == ['pw', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz', 'rw', 'rx', 'ry', 'rz', 'sw', 'sx', 'sy', 'sz']