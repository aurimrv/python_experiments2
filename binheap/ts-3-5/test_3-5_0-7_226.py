import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from binheap import Binheap

@pytest.fixture
def binheap():
    return Binheap()

def test_init(binheap):
    assert binheap.container == [None]

def test_push(binheap):
    binheap.push(5)
    assert binheap.container == [None, 5]
    binheap.push(10)
    assert binheap.container == [None, 10, 5]

def test_pop(binheap):
    binheap.push(5)
    binheap.push(10)
    binheap.pop()
    assert binheap.container == [None, 5]

def test_display(binheap):
    binheap.push(1)
    binheap.push(2)
    binheap.push(3)
    assert binheap.display() == ' 3 \n1 2 \n'