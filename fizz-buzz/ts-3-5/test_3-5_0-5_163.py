import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz():
    assert fizz_buzz(1) == ['1']

def test_fizz_buzz_divisible_by_3():
    assert fizz_buzz(3) == ['1', '2', 'Fizz']

def test_fizz_buzz_divisible_by_5():
    assert fizz_buzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']

def test_fizz_buzz_divisible_by_3_and_5():
    assert fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def test_fizz_buzz_large_number():
    assert fizz_buzz(20) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz']