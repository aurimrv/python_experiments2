import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test empty string
    assert combinations_of_word('') == []

    # Test single character word
    assert combinations_of_word('a') == ['a']

    # Test word with all unique characters
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']

    # Test word with repeated characters
    assert combinations_of_word('aab') == ['a', 'aa', 'aab', 'a', 'ab', 'b']

def test_combinations_of_phone_input():
    # Test phone input with single number
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test phone input with two numbers
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test phone input with repeated numbers
    assert combinations_of_phone_input('22') == ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

    # Test phone input with different numbers
    assert combinations_of_phone_input('29') == ['aw', 'ax', 'ay', 'az', 'bw', 'bx', 'by', 'bz', 'cw', 'cx', 'cy', 'cz']