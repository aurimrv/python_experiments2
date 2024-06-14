import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import combinations

def test_combinations_of_word():
    # Test when input is an empty string
    assert combinations.combinations_of_word('') == []

    # Test when input is a single character
    assert combinations.combinations_of_word('a') == ['a']

    # Test when input is a word with multiple characters
    assert combinations.combinations_of_word('cat') == ['c', 'ca', 'cat', 'a', 'at', 't']

def test_combinations_of_phone_input():
    # Test when input is a single digit
    assert combinations.combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test when input has multiple digits
    assert combinations.combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test when input has repeating digits
    assert combinations.combinations_of_phone_input('22') == ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']