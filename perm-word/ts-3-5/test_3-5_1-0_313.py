import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from permutations import permutations_of_word

def test_permutations_of_word_empty_string():
    assert permutations_of_word('') == ['']

def test_permutations_of_word_single_char():
    assert permutations_of_word('a') == ['a']

def test_permutations_of_word_two_chars():
    assert permutations_of_word('ab') == ['ab', 'ba']

def test_permutations_of_word_three_chars():
    assert permutations_of_word('abc') == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def test_permutations_of_word_repeated_chars():
    assert set(permutations_of_word('aab')) == set(['aab', 'aba', 'baa'])

def test_permutations_of_word_long_string():
    assert set(permutations_of_word('abcd')) == set(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 
                                            'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 
                                            'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 
                                            'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])