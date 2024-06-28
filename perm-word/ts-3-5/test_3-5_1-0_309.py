import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from permutations import permutations_of_word

def test_permutations_of_word():
    assert permutations_of_word('abc') == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert permutations_of_word('123') == ['123', '132', '213', '231', '312', '321']

def test_permutations_of_word_empty_string():
    assert permutations_of_word('') == ['']

def test_permutations_of_word_single_letter():
    assert permutations_of_word('a') == ['a']

def test_permutations_of_word_repeated_characters():
    assert permutations_of_word('abb') == ['abb', 'abb', 'bab', 'bba', 'bab', 'bba']

def test_permutations_of_word_longer_string():
    assert permutations_of_word('abcd') == ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                                             'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                                             'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                                             'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']