import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from permutations import permutations_of_word

def test_permutations_of_word():
    # Test empty string
    assert permutations_of_word('') == ['']

    # Test single character string
    assert permutations_of_word('a') == ['a']

    # Test string with repeated characters
    assert set(permutations_of_word('aab')) == set(['aab', 'aba', 'baa'])

    # Test string with all unique characters
    assert set(permutations_of_word('abc')) == set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    # Test longer string
    assert len(permutations_of_word('hello')) == 120  # 5! permutations