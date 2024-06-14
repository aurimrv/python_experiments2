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
    assert combinations_of_word('xyz') == ['x', 'xy', 'xyz', 'y', 'yz', 'z']

def test_combinations_of_word_empty_input():
    assert combinations_of_word('') == []

def test_combinations_of_phone_input():
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert combinations_of_phone_input('567') == ['jmp', 'jmq', 'jmr', 'jms', 'jnp', 'jnq', 'jnr', 'jns', 'jop', 'joq', 'jor', 'jos', 'kmp', 'kmq', 'kmr', 'kms', 'knp', 'knq', 'knr', 'kns', 'kop', 'koq', 'kor', 'kos', 'lmp', 'lmq', 'lmr', 'lms', 'lnp', 'lnq', 'lnr', 'lns', 'lop', 'loq', 'lor', 'los']
    assert combinations_of_phone_input('9') == ['w', 'x', 'y', 'z']

def test_combinations_of_phone_input_single_digit():
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']
    assert combinations_of_phone_input('7') == ['p', 'q', 'r', 's']
