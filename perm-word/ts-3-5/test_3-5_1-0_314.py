import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from permutations import permutations_of_word

def test_permutations_of_word():
    assert permutations_of_word('abc') == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert permutations_of_word('abcd') == ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
    assert permutations_of_word('a') == ['a']

def test_permute_function():
    assert permutations_of_word('') == ['']
    assert permutations_of_word('aa') == ['aa', 'aa']
    assert permutations_of_word('aaa') == ['aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa']