import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_divisible_by_three():
    result = fizz_buzz(3)
    assert result == ["1", "2", "Fizz"]

def test_fizz_buzz_divisible_by_five():
    result = fizz_buzz(5)
    assert result == ["1", "2", "Fizz", "4", "Buzz"]

def test_fizz_buzz_divisible_by_three_and_five():
    result = fizz_buzz(15)
    assert result == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

def test_fizz_buzz_non_divisible_by_three_or_five():
    result = fizz_buzz(7)
    assert result == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"]

def test_fizz_buzz_zero_input():
    result = fizz_buzz(0)
    assert result == []