import os
import sys
import pytest
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_returns_correct_output():
    expected_output = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert fizz_buzz(15) == expected_output

def test_fizz_buzz_with_small_number():
    expected_output = ["1"]
    assert fizz_buzz(1) == expected_output

def test_fizz_buzz_with_divisible_by_3():
    expected_output = ["1", "2", "Fizz"]
    assert fizz_buzz(3) == expected_output

def test_fizz_buzz_with_divisible_by_5():
    expected_output = ["1", "2", "Fizz", "4", "Buzz"]
    assert fizz_buzz(5) == expected_output