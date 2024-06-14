import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import pytest
from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    assert combinations_of_word("") == []
    assert combinations_of_word("a") == ["a"]
    assert combinations_of_word("abc") == ['a', 'ab', 'abc', 'b', 'bc', 'c']

def test_combinations_of_phone_input():
    assert combinations_of_phone_input("2") == ['a', 'b', 'c']
    assert combinations_of_phone_input("23") == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert combinations_of_phone_input("567") == ['jmp', 'jmq', 'jmr', 'jms', 'jnp', 'jnq', 'jnr', 'jns', 'jop', 'joq', 'jor', 'jos', 'kmp', 'kmq', 'kmr', 'kms', 'knp', 'knq', 'knr', 'kns', 'kop', 'koq', 'kor', 'kos', 'lmp', 'lmq', 'lmr', 'lms', 'lnp', 'lnq', 'lnr', 'lns', 'lop', 'loq', 'lor', 'los']