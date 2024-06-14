import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)
import combinations

import pytest

@pytest.mark.parametrize("input_str, expected_output",
                         [
                             ("abc", ['a', 'ab', 'abc', 'b', 'bc', 'c']),
                             ("123", ['1', '12', '123', '2', '23', '3']),
                             ("", [])
                         ])
def test_combinations_of_word(input_str, expected_output):
    assert combinations.combinations_of_word(input_str) == expected_output

@pytest.mark.parametrize("input_str, expected_output",
                         [
                             ("23", ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
                             ("9", ['w', 'x', 'y', 'z']),
                             ("234", ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi'])
                         ])
def test_combinations_of_phone_input(input_str, expected_output):
    assert combinations.combinations_of_phone_input(input_str) == expected_output