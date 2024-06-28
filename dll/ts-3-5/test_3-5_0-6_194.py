import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

def test_node_init():
    node = Node(5)
    assert node.data == 5
    assert node.next is None
    assert node.prev is None

def test_double_linked_list_init():
    dll = DoubleLinkedList([1, 2, 3])
    assert dll.head.data == 3
    assert dll.tail.data == 1
    assert dll._length == 3

def test_push():
    dll = DoubleLinkedList()
    dll.push(10)
    assert dll.head.data == 10
    assert dll.tail.data == 10
    assert dll._length == 1

def test_pop():
    dll = DoubleLinkedList([1, 2, 3])
    popped = dll.pop()
    assert popped == 3
    assert dll.head.data == 2
    assert dll.tail.data == 1
    assert dll._length == 2

def test_append():
    dll = DoubleLinkedList()
    dll.append(5)
    assert dll.head.data == 5
    assert dll.tail.data == 5
    assert dll._length == 1

def test_shift():
    dll = DoubleLinkedList([1, 2, 3])
    shifted = dll.shift()
    assert shifted == 1
    assert dll.head.data == 3
    assert dll.tail.data == 2
    assert dll._length == 2

def test_remove():
    dll = DoubleLinkedList([1, 2, 3])
    dll.remove(2)
    assert dll.head.data == 3
    assert dll.tail.data == 1
    assert dll._length == 2
    with pytest.raises(ValueError):
        dll.remove(5)