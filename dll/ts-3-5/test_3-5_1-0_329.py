import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

def test_node_repr():
    n = Node(5)
    assert repr(n) == "Value: 5"

def test_push_pop():
    dll = DoubleLinkedList()
    dll.push(10)
    dll.push(20)
    assert dll.pop() == 20
    assert dll.pop() == 10

def test_append_shift():
    dll = DoubleLinkedList([1, 2, 3])
    dll.append(4)
    dll.append(5)
    assert dll.shift() == 5
    assert dll.shift() == 4

def test_remove():
    dll = DoubleLinkedList([1, 2, 3, 4, 5])
    dll.remove(3)
    assert dll._repr() == [5, 4, 2, 1]

def test_empty_list_behavior():
    dll = DoubleLinkedList()
    with pytest.raises(IndexError):
        dll.pop()
    with pytest.raises(IndexError):
        dll.shift()
    with pytest.raises(ValueError):
        dll.remove(99)