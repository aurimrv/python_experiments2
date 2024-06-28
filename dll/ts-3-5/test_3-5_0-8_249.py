import os
import sys
import pytest
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

@pytest.fixture
def empty_dll():
    return DoubleLinkedList()

@pytest.fixture
def dll_with_values():
    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.append(3)
    return dll

def test_node_repr():
    node = Node(5)
    assert str(node) == "Value: 5"

def test_dll_push(empty_dll):
    empty_dll.push(10)
    assert empty_dll.head.data == 10
    assert empty_dll.tail.data == 10

def test_dll_pop(dll_with_values):
    assert dll_with_values.pop() == 2
    assert dll_with_values.head.data == 1

def test_dll_append(empty_dll):
    empty_dll.append(7)
    assert empty_dll.tail.data == 7
    assert empty_dll.head.data == 7

def test_dll_shift(dll_with_values):
    assert dll_with_values.shift() == 3
    assert dll_with_values.tail.data == 1

def test_dll_remove(dll_with_values):
    dll_with_values.remove(2)
    assert dll_with_values.head.data == 1
    assert dll_with_values.tail.data == 3

def test_dll_remove_non_existing(dll_with_values):
    with pytest.raises(ValueError):
        dll_with_values.remove(5)