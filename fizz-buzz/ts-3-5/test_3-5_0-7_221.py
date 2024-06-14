import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_divisible_by_3():
    result = fizz_buzz(9)
    assert result[2] == "Fizz"
    assert result[5] == "Fizz"

def test_fizz_buzz_divisible_by_5():
    result = fizz_buzz(10)
    assert result[4] == "Buzz"
    assert result[9] == "Buzz"

def test_fizz_buzz_divisible_by_3_and_5():
    result = fizz_buzz(15)
    assert result[14] == "FizzBuzz"

def test_fizz_buzz_not_divisible_by_3_or_5():
    result = fizz_buzz(7)
    assert result[0] == "1"
    assert result[1] == "2"
    assert result[3] == "4"
    assert result[6] == "7"