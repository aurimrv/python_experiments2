import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_returns_list():
    result = fizz_buzz(15)
    assert isinstance(result, list)

def test_fizz_buzz_correct_output_length():
    result = fizz_buzz(15)
    assert len(result) == 15

def test_fizz_buzz_returns_fizz_for_multiples_of_3():
    result = fizz_buzz(15)
    assert result[2] == 'Fizz'
    assert result[5] == 'Fizz'
    assert result[11] == 'Fizz'

def test_fizz_buzz_returns_buzz_for_multiples_of_5():
    result = fizz_buzz(15)
    assert result[4] == 'Buzz'
    assert result[9] == 'Buzz'

def test_fizz_buzz_returns_fizzbuzz_for_multiples_of_3_and_5():
    result = fizz_buzz(15)
    assert result[14] == 'FizzBuzz'

def test_fizz_buzz_returns_numbers_for_non_divisible_numbers():
    result = fizz_buzz(15)
    assert result[0] == '1'
    assert result[1] == '2'
    assert result[3] == '4'
    assert result[6] == '7'
    assert result[10] == '11'
    assert result[12] == '13'
    assert result[13] == '14'