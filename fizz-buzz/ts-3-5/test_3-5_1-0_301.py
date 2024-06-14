import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz_returns_correct_list():
    result = fizz_buzz(5)
    assert result == ['1', '2', 'Fizz', '4', 'Buzz']

def test_fizz_buzz_includes_fizz():
    result = fizz_buzz(6)
    assert 'Fizz' in result

def test_fizz_buzz_includes_buzz():
    result = fizz_buzz(10)
    assert 'Buzz' in result

def test_fizz_buzz_includes_fizzbuzz():
    result = fizz_buzz(15)
    assert 'FizzBuzz' in result

def test_fizz_buzz_with_1_returns_1():
    result = fizz_buzz(1)
    assert result == ['1']