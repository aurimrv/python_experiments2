import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import fizz_buzz

def test_fizz_buzz_divisible_by_both():
    assert fizz_buzz.fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def test_fizz_buzz_divisible_by_three():
    assert fizz_buzz.fizz_buzz(6) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz']

def test_fizz_buzz_divisible_by_five():
    assert fizz_buzz.fizz_buzz(10) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']

def test_fizz_buzz_not_divisible():
    assert fizz_buzz.fizz_buzz(4) == ['1', '2', 'Fizz', '4']