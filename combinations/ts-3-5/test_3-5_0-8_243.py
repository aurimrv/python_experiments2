import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test case for empty string
    assert combinations_of_word('') == []

    # Test case for a single character
    assert combinations_of_word('a') == ['a']

    # Test case for a word with multiple combinations
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']

def test_combinations_of_phone_input():
    # Test case for a single digit
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']

    # Test case for multiple digits
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    # Test case for a longer input
    assert combinations_of_phone_input('789') == ['ptw', 'ptx', 'pty', 'ptz', 'puw', 'pux', 'puy', 'puz', 'pvw', 'pvx', 'pvy', 'pvz', 'qtw', 'qtx', 'qty', 'qtz', 'quw', 'qux', 'quy', 'quz', 'qvw', 'qvx', 'qvy', 'qvz', 'rtw', 'rtx', 'rty', 'rtz', 'ruw', 'rux', 'ruy', 'ruz', 'rvw', 'rvx', 'rvy', 'rvz', 'stw', 'stx', 'sty', 'stz', 'suw', 'sux', 'suy', 'suz', 'svw', 'svx', 'svy', 'svz']
