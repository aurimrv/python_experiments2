import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_with_15_elements():
    result = fizz_buzz(15)
    expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    assert result == expected

def test_fizz_buzz_with_5_elements():
    result = fizz_buzz(5)
    expected = ['1', '2', 'Fizz', '4', 'Buzz']
    assert result == expected

def test_fizz_buzz_with_1_element():
    result = fizz_buzz(1)
    expected = ['1']
    assert result == expected

def test_fizz_buzz_with_10_elements():
    result = fizz_buzz(10)
    expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
    assert result == expected