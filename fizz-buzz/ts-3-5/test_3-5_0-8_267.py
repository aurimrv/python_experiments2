import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

import pytest

def test_fizz_buzz_divisible_by_3():
    result = fizz_buzz(3)
    assert result == ['1', '2', 'Fizz']

def test_fizz_buzz_divisible_by_5():
    result = fizz_buzz(5)
    assert result == ['1', '2', 'Fizz', '4', 'Buzz']

def test_fizz_buzz_divisible_by_3_and_5():
    result = fizz_buzz(15)
    assert result == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def test_fizz_buzz_non_divisible_by_3_or_5():
    result = fizz_buzz(2)
    assert result == ['1', '2']

def test_fizz_buzz_large_number():
    result = fizz_buzz(100)
    assert result[98] == 'Fizz'
    assert result[99] == 'Buzz'
    assert result[14] == 'FizzBuzz'

def test_fizz_buzz_empty_input():
    result = fizz_buzz(0)
    assert result == []