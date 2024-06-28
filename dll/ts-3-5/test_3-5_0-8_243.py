import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

import pytest

# Test Node class
def test_node_repr():
    node = Node(5)
    assert repr(node) == "Value: 5"

# Test DoubleLinkedList class
def test_double_linked_list_push():
    dll = DoubleLinkedList()
    dll.push(1)
    assert dll.head.data == 1

def test_double_linked_list_pop():
    dll = DoubleLinkedList([1, 2, 3])
    popped_val = dll.pop()
    assert popped_val == 3

def test_double_linked_list_append():
    dll = DoubleLinkedList()
    dll.append(1)
    assert dll.tail.data == 1

def test_double_linked_list_shift():
    dll = DoubleLinkedList([1, 2, 3])
    shifted_val = dll.shift()
    assert shifted_val == 1

def test_double_linked_list_remove():
    dll = DoubleLinkedList([1, 2, 3])
    dll.remove(2)
    assert dll._repr() == [3, 1]

def test_double_linked_list_empty_pop():
    dll = DoubleLinkedList()
    with pytest.raises(IndexError):
        dll.pop()

def test_double_linked_list_empty_shift():
    dll = DoubleLinkedList()
    with pytest.raises(IndexError):
        dll.shift()

def test_double_linked_list_remove_non_existent():
    dll = DoubleLinkedList([1, 2, 3])
    with pytest.raises(ValueError):
        dll.remove(4)