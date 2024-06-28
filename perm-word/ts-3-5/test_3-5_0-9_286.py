import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from permutations import permutations_of_word

def test_permutations_of_word_empty_string():
    result = permutations_of_word('')
    assert result == ['']

def test_permutations_of_word_single_letter():
    result = permutations_of_word('a')
    assert result == ['a']

def test_permutations_of_word_two_letters():
    result = permutations_of_word('ab')
    assert result == ['ab', 'ba']

def test_permutations_of_word_three_letters():
    result = permutations_of_word('abc')
    assert result == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
