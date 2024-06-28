import os
import sys
import pytest

# Add project directory to sys path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

# Test Node class
def test_node_init():
    node = Node(5)
    assert node.data == 5

def test_node_repr():
    node = Node(10)
    assert str(node) == "Value: 10"

# Test DoubleLinkedList class
def test_dll_init():
    dll = DoubleLinkedList([1, 2, 3, 4, 5])
    assert dll.head.data == 5
    assert dll.tail.data == 1
    assert dll._length == 5

def test_dll_push():
    dll = DoubleLinkedList()
    dll.push(10)
    assert dll.head.data == 10
    assert dll.tail.data == 10
    assert dll._length == 1

def test_dll_pop():
    dll = DoubleLinkedList([1, 2, 3])
    popped_val = dll.pop()
    assert popped_val == 3
    assert dll.head.data == 2
    assert dll._length == 2

def test_dll_append():
    dll = DoubleLinkedList()
    dll.append(20)
    assert dll.tail.data == 20
    assert dll.head.data == 20
    assert dll._length == 1

def test_dll_shift():
    dll = DoubleLinkedList([1, 2, 3])
    shifted_val = dll.shift()
    assert shifted_val == 1
    assert dll.tail.data == 2
    assert dll._length == 2

def test_dll_remove():
    dll = DoubleLinkedList([1, 2, 3, 4])
    dll.remove(3)
    assert dll._length == 3
    dll.remove(1)
    assert dll._length == 2

def test_dll_remove_exception():
    dll = DoubleLinkedList([1, 2, 3])
    with pytest.raises(ValueError):
        dll.remove(5)

def test_dll_repr():
    dll = DoubleLinkedList([1, 2, 3])
    dll_repr = dll._repr()
    assert dll_repr == [3, 2, 1]