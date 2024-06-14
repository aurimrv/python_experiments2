import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_divisible_by_three():
    assert fizz_buzz(3) == ['1', '2', 'Fizz']

def test_fizz_buzz_divisible_by_five():
    assert fizz_buzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']

def test_fizz_buzz_divisible_by_fifteen():
    assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def test_fizz_buzz_non_divisible_numbers():
    assert fizz_buzz(4) == ['1', '2', 'Fizz', '4']

def test_fizz_buzz_zero_input():
    assert fizz_buzz(0) == []

def test_fizz_buzz_negative_input():
    assert fizz_buzz(-5) == []