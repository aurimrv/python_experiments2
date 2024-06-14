import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_one():
    assert fizz_buzz(1) == ['1']

def test_fizz_buzz_fifteen():
    assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def test_fizz_buzz_negative():
    assert fizz_buzz(-5) == []

def test_fizz_buzz_zero():
    assert fizz_buzz(0) == []

def test_fizz_buzz_large_number():
    result = fizz_buzz(1000)
    assert len(result) == 1000
    assert result[2] == 'Fizz'
    assert result[4] == 'Buzz'
    assert result[14] == 'FizzBuzz'