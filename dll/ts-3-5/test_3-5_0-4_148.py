import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

@pytest.fixture
def dll_empty():
    return DoubleLinkedList()

@pytest.fixture
def dll_filled():
    return DoubleLinkedList([1, 2, 3, 4, 5])

def test_node_repr():
    node = Node(10)
    assert repr(node) == "Value: 10"

def test_dll_init_empty(dll_empty):
    assert dll_empty.head is None
    assert dll_empty.tail is None
    assert dll_empty._length == 0

def test_dll_init_filled(dll_filled):
    assert dll_filled.head.data == 5
    assert dll_filled.tail.data == 1
    assert dll_filled._length == 5

def test_dll_push(dll_empty):
    dll_empty.push(100)
    assert dll_empty.head.data == 100
    assert dll_empty.tail.data == 100
    assert dll_empty._length == 1

def test_dll_pop(dll_filled):
    assert dll_filled.pop() == 5
    assert dll_filled.head.data == 4
    assert dll_filled._length == 4

def test_dll_append(dll_empty):
    dll_empty.append(200)
    assert dll_empty.head.data == 200
    assert dll_empty.tail.data == 200
    assert dll_empty._length == 1

def test_dll_shift(dll_filled):
    assert dll_filled.shift() == 1
    assert dll_filled.tail.data == 2
    assert dll_filled._length == 4

def test_dll_remove(dll_filled):
    dll_filled.remove(3)
    assert dll_filled.head.data == 5
    assert dll_filled.tail.data == 1
    assert dll_filled._length == 4
    with pytest.raises(ValueError):
        dll_filled.remove(10)

def test_dll_repr(dll_filled):
    assert dll_filled._repr() == [5, 4, 3, 2, 1]