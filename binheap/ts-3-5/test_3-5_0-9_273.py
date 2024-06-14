import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from binheap import Binheap

import pytest

@pytest.fixture
def new_binheap():
    return Binheap()

@pytest.fixture
def filled_binheap():
    return Binheap([9, 5, 7, 3, 1])

def test_init_empty(new_binheap):
    assert new_binheap.container == [None]

def test_init_with_data(filled_binheap):
    assert filled_binheap.container == [None, 9, 5, 7, 3, 1]

def test_balance(filled_binheap):
    filled_binheap._balance()
    assert filled_binheap.container == [None, 9, 5, 7, 3, 1]

def test_push(new_binheap):
    new_binheap.push(10)
    assert new_binheap.container == [None, 10]

def test_pop(filled_binheap):
    filled_binheap.pop()
    assert filled_binheap.container == [None, 7, 5, 3, 1]

def test_display(filled_binheap):
    assert filled_binheap.display() == '  9 \n 5 7 \n3 1 \n'