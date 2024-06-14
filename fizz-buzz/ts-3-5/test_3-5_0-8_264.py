import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from fizz_buzz import fizz_buzz

def test_fizz_buzz():
    # Test case for numbers not divisible by 3 or 5
    assert fizz_buzz(2) == ['1', '2']

    # Test case for numbers divisible by 3 but not 5
    assert fizz_buzz(4) == ['1', '2', 'Fizz', '4']

    # Test case for numbers divisible by 5 but not 3
    assert fizz_buzz(6) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz']

    # Test case for numbers divisible by both 3 and 5
    assert fizz_buzz(16) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16']