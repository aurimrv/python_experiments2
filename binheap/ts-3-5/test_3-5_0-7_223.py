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
    binheap.push(5)
    binheap.push(10)
    binheap.push(15)
    assert binheap.display() == ' 15 \n5 10 \n'