import pytest
from factorial import factorial

def test_factorial():
    assert factorial(0) == 0
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(10) == 3628800

