import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

class TestCombinations:
    
    def test_combinations_of_word(self):
        # Test empty string
        assert combinations_of_word('') == []
        
        # Test single character string
        assert combinations_of_word('a') == ['a']
        
        # Test multiple character string
        assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']
        
    def test_combinations_of_phone_input(self):
        # Test single digit input
        assert combinations_of_phone_input('2') == ['a', 'b', 'c']
        
        # Test two-digit input
        assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        
        # Test input with repeating digits
        assert combinations_of_phone_input('22') == ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']