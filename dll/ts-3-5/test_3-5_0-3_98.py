import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

@pytest.fixture
def setup_dll():
    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    return dll

def test_push(setup_dll):
    assert setup_dll.head.data == 3
    assert setup_dll.tail.data == 1
    assert setup_dll._length == 3

def test_pop(setup_dll):
    assert setup_dll.pop() == 3
    assert setup_dll.head.data == 2
    assert setup_dll._length == 2

def test_append(setup_dll):
    setup_dll.append(4)
    assert setup_dll.tail.data == 4
    assert setup_dll._length == 4

def test_shift(setup_dll):
    assert setup_dll.shift() == 1
    assert setup_dll.tail.data == 2
    assert setup_dll._length == 2

def test_remove(setup_dll):
    setup_dll.remove(2)
    assert setup_dll.head.data == 3
    assert setup_dll.tail.data == 1
    assert setup_dll._length == 2

def test_remove_nonexistent(setup_dll):
    with pytest.raises(ValueError):
        setup_dll.remove(5)