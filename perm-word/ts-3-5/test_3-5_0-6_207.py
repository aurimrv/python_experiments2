import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from permutations import permutations_of_word

def test_permutations_of_word_empty_string():
    assert permutations_of_word('') == ['']

def test_permutations_of_word_single_letter():
    assert permutations_of_word('a') == ['a']

def test_permutations_of_word_two_letters():
    assert set(permutations_of_word('ab')) == {'ab', 'ba'}

def test_permutations_of_word_three_letters():
    assert set(permutations_of_word('abc')) == {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}

def test_permutations_of_word_repeated_letters():
    assert set(permutations_of_word('aab')) == {'aab', 'aba', 'baa'}

def test_permutations_of_word_long_string():
    assert len(permutations_of_word('abcd')) == 24