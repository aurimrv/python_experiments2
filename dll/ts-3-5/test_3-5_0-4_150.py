import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

import pytest

@pytest.fixture
def empty_dll():
    return DoubleLinkedList()

@pytest.fixture
def dll_with_data():
    return DoubleLinkedList([1, 2, 3])

def test_node_repr():
    node = Node(5)
    assert repr(node) == "Value: 5"

def test_dll_init_empty(empty_dll):
    assert empty_dll.head is None
    assert empty_dll.tail is None
    assert empty_dll._length == 0

def test_dll_init_with_data(dll_with_data):
    assert dll_with_data.head.data == 3
    assert dll_with_data.tail.data == 1
    assert dll_with_data._length == 3

def test_dll_push(empty_dll):
    empty_dll.push(10)
    assert empty_dll.head.data == 10
    assert empty_dll.tail.data == 10
    assert empty_dll._length == 1

def test_dll_pop(dll_with_data):
    assert dll_with_data.pop() == 3
    assert dll_with_data.head.data == 2
    assert dll_with_data._length == 2

def test_dll_append(empty_dll):
    empty_dll.append(20)
    assert empty_dll.head.data == 20
    assert empty_dll.tail.data == 20
    assert empty_dll._length == 1

def test_dll_shift(dll_with_data):
    assert dll_with_data.shift() == 1
    assert dll_with_data.tail.data == 2
    assert dll_with_data._length == 2

def test_dll_remove(dll_with_data):
    dll_with_data.remove(2)
    assert dll_with_data.head.data == 3
    assert dll_with_data.tail.data == 1
    assert dll_with_data._length == 2

def test_dll_remove_invalid(dll_with_data):
    with pytest.raises(ValueError):
        dll_with_data.remove(5)

def test_dll_repr(dll_with_data):
    assert dll_with_data._repr() == [3, 2, 1]