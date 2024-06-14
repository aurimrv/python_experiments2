import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert combinations_of_word('123') == ['1', '12', '123', '2', '23', '3']
    assert combinations_of_word('xy') == ['x', 'xy', 'y']

def test_combinations_of_phone_input():
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']
    assert combinations_of_phone_input('34') == ['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']
    assert combinations_of_phone_input('79') == ['pw', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz', 'rw', 'rx', 'ry', 'rz', 'sw', 'sx', 'sy', 'sz']