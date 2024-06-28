import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

import pytest

@pytest.fixture
def dll_empty():
    return DoubleLinkedList()

@pytest.fixture
def dll_filled():
    dll = DoubleLinkedList([1, 2, 3, 4])
    return dll

def test_node_repr():
    node = Node(5)
    assert repr(node) == 'Value: 5'

def test_dll_init_empty(dll_empty):
    assert dll_empty.head is None
    assert dll_empty.tail is None
    assert dll_empty._length == 0

def test_dll_init_filled(dll_filled):
    assert dll_filled.head.data == 4
    assert dll_filled.tail.data == 1
    assert dll_filled._length == 4

def test_dll_push(dll_empty):
    dll_empty.push(10)
    assert dll_empty.head.data == 10
    assert dll_empty.tail.data == 10
    assert dll_empty._length == 1

def test_dll_pop(dll_filled):
    popped_val = dll_filled.pop()
    assert popped_val == 4
    assert dll_filled.head.data == 3
    assert dll_filled._length == 3

def test_dll_append(dll_empty):
    dll_empty.append(20)
    assert dll_empty.head.data == 20
    assert dll_empty.tail.data == 20
    assert dll_empty._length == 1

def test_dll_shift(dll_filled):
    shifted_val = dll_filled.shift()
    assert shifted_val == 1
    assert dll_filled.tail.data == 2
    assert dll_filled._length == 3

def test_dll_remove(dll_filled):
    dll_filled.remove(2)
    assert dll_filled.head.data == 4
    assert dll_filled.tail.data == 1
    assert dll_filled._length == 3
    with pytest.raises(ValueError):
        dll_filled.remove(5)