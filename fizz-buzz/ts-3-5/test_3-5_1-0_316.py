import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

import pytest

@pytest.mark.parametrize("n, expected", [
    (1, ['1']),
    (5, ['1', '2', 'Fizz', '4', 'Buzz']),
    (15, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']),
])
def test_fizz_buzz(n, expected):
    assert fizz_buzz(n) == expected

def test_fizz_buzz_empty():
    assert fizz_buzz(0) == []