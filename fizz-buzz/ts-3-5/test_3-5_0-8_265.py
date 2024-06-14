import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_divisible_by_3():
    result = fizz_buzz(6)
    assert result == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz']

def test_fizz_buzz_divisible_by_5():
    result = fizz_buzz(10)
    assert result == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']

def test_fizz_buzz_divisible_by_both_3_and_5():
    result = fizz_buzz(15)
    assert result == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def test_fizz_buzz_n_is_1():
    result = fizz_buzz(1)
    assert result == ['1']

def test_fizz_buzz_n_is_0():
    result = fizz_buzz(0)
    assert result == []

def test_fizz_buzz_n_is_negative():
    result = fizz_buzz(-5)
    assert result == []