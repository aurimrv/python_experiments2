import os
import sys
import pytest

module_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(module_path, '..'))
sys.path.append(project_path)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_divisible_by_3():
    assert fizz_buzz(3) == ['1', '2', 'Fizz']

def test_fizz_buzz_divisible_by_5():
    assert fizz_buzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']

def test_fizz_buzz_divisible_by_3_and_5():
    assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def test_fizz_buzz_all_numbers():
    assert fizz_buzz(1) == ['1']

def test_fizz_buzz_negative_number():
    assert fizz_buzz(-10) == []

def test_fizz_buzz_zero():
    assert fizz_buzz(0) == []