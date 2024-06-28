import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

# Node class tests
def test_node_init():
    node = Node(5)
    assert node.data == 5

def test_node_repr():
    node = Node(7)
    assert repr(node) == "Value: 7"

# DoubleLinkedList class tests
def test_dll_push():
    dll = DoubleLinkedList()
    dll.push(1)
    assert dll.head.data == 1

def test_dll_pop():
    dll = DoubleLinkedList([1, 2, 3])
    assert dll.pop() == 3

def test_dll_append():
    dll = DoubleLinkedList()
    dll.append(4)
    assert dll.tail.data == 4

def test_dll_shift():
    dll = DoubleLinkedList([1, 2, 3])
    assert dll.shift() == 1

def test_dll_remove():
    dll = DoubleLinkedList([1, 2, 3, 4, 5])
    dll.remove(3)
    assert dll._length == 4

def test_dll_repr():
    dll = DoubleLinkedList([1, 2, 3])
    assert dll._repr() == [3, 2, 1]