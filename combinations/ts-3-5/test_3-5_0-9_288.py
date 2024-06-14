import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    word = "abc"
    expected_output = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert combinations_of_word(word) == expected_output

    word = "dog"
    expected_output = ['d', 'do', 'dog', 'o', 'og', 'g']
    assert combinations_of_word(word) == expected_output

def test_combinations_of_phone_input():
    phone_input = "23"
    expected_output = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert combinations_of_phone_input(phone_input) == expected_output

    phone_input = "78"
    expected_output = ['pt', 'pu', 'pv', 'qt', 'qu', 'qv', 'rt', 'ru', 'rv', 'st', 'su', 'sv']
    assert combinations_of_phone_input(phone_input) == expected_output