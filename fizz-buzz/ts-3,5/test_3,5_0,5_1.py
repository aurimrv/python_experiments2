import fizz_buzz

def test_fizz_buzz_divisible_by_3():
    assert fizz_buzz.fizz_buzz(3) == ['1', '2', 'Fizz']

def test_fizz_buzz_divisible_by_5():
    assert fizz_buzz.fizz_buzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']

def test_fizz_buzz_divisible_by_3_and_5():
    assert fizz_buzz.fizz_buzz(15) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

def test_fizz_buzz_not_divisible_by_3_or_5():
    assert fizz_buzz.fizz_buzz(7) == ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7']