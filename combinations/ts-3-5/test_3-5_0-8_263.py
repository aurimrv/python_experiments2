import pytest
import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from combinations import combinations_of_word, combinations_of_phone_input

def test_combinations_of_word():
    # Test empty string
    assert combinations_of_word('') == []
    
    # Test single character
    assert combinations_of_word('a') == ['a']
    
    # Test word with unique characters
    assert combinations_of_word('abc') == ['a', 'ab', 'abc', 'b', 'bc', 'c']
    
    # Test word with repeating characters
    assert combinations_of_word('aab') == ['a', 'aa', 'aab', 'a', 'ab', 'b']

def test_combinations_of_phone_input():
    # Test input '2'
    assert combinations_of_phone_input('2') == ['a', 'b', 'c']
    
    # Test input '23'
    assert combinations_of_phone_input('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    
    # Test input '45'
    assert combinations_of_phone_input('45') == ['gj', 'gk', 'gl', 'hj', 'hk', 'hl', 'ij', 'ik', 'il']
    
    # Test input '999'
    assert combinations_of_phone_input('999') == ['www', 'wwx', 'wwy', 'wwz', 'wxw', 'wxx', 'wxy', 'wxz', 'wyw', 'wyx', 'wyy', 'wyz', 'wzw', 'wzx', 'wzy', 'wzz', 'xww', 'xwx', 'xwy', 'xwz', 'xxw', 'xxx', 'xxy', 'xxz', 'xyw', 'xyx', 'xyy', 'xyz', 'xzw', 'xzx', 'xzy', 'xzz', 'yww', 'ywx', 'ywy', 'ywz', 'yxw', 'yxx', 'yxy', 'yxz', 'yyw', 'yyx', 'yyy', 'yyz', 'yzw', 'yzx', 'yzy', 'yzz', 'zww', 'zwx', 'zwy', 'zwz', 'zxw', 'zxx', 'zxy', 'zxz', 'zyw', 'zyx', 'zyy', 'zyz', 'zzw', 'zzx', 'zzy', 'zzz']
