import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    string = "abc"
    expected_output = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert combinations_of_word(string) == expected_output

    string = "123"
    expected_output = ['1', '12', '123', '2', '23', '3']
    assert combinations_of_word(string) == expected_output

def test_combinations_of_phone_input():
    string = "23"
    expected_output = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert combinations_of_phone_input(string) == expected_output

    string = "789"
    expected_output = ['ptw', 'ptx', 'pty', 'ptz', 'puw', 'pux', 'puy', 'puz', 'pvw', 'pvx', 'pvy', 'pvz', 'qtw', 'qtx', 'qty', 'qtz', 'quw', 'qux', 'quy', 'quz', 'qvw', 'qvx', 'qvy', 'qvz', 'rtw', 'rtx', 'rty', 'rtz', 'ruw', 'rux', 'ruy', 'ruz', 'rvw', 'rvx', 'rvy', 'rvz', 'stw', 'stx', 'sty', 'stz', 'suw', 'sux', 'suy', 'suz', 'svw', 'svx', 'svy', 'svz']
    assert combinations_of_phone_input(string) == expected_output