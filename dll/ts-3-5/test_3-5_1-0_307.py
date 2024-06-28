import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

def test_node_repr():
    node = Node(10)
    assert repr(node) == "Value: 10"

def test_dll_init():
    dll = DoubleLinkedList([1, 2, 3])
    assert dll.head.data == 3
    assert dll.tail.data == 1
    assert dll._length == 3

def test_dll_push():
    dll = DoubleLinkedList()
    dll.push(5)
    assert dll.head.data == 5
    assert dll.tail.data == 5

def test_dll_pop():
    dll = DoubleLinkedList([1, 2, 3])
    data = dll.pop()
    assert data == 3
    assert dll.head.data == 2
    assert dll._length == 2

def test_dll_append():
    dll = DoubleLinkedList([1, 2, 3])
    dll.append(4)
    assert dll.tail.data == 4
    assert dll._length == 4

def test_dll_shift():
    dll = DoubleLinkedList([1, 2, 3])
    data = dll.shift()
    assert data == 1
    assert dll.tail.data == 2
    assert dll._length == 2

def test_dll_remove():
    dll = DoubleLinkedList([1, 2, 3])
    dll.remove(2)
    assert dll.head.data == 3
    assert dll.tail.data == 1
    assert dll._length == 2
    with pytest.raises(ValueError):
        dll.remove(5)