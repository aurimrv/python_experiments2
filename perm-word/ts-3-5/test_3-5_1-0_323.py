import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from permutations import permutations_of_word

def test_permutations_of_word_empty_string():
    assert permutations_of_word('') == ['']

def test_permutations_of_word_single_character():
    assert permutations_of_word('a') == ['a']

def test_permutations_of_word_two_characters():
    assert permutations_of_word('ab') == ['ab', 'ba']

def test_permutations_of_word_three_characters():
    assert permutations_of_word('abc') == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']