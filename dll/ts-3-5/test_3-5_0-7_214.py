import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

import pytest

@pytest.fixture
def empty_list():
    return DoubleLinkedList()

@pytest.fixture
def filled_list():
    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    return dll

def test_node_repr():
    node = Node(5)
    assert repr(node) == "Value: 5"

def test_empty_list_creation(empty_list):
    assert empty_list.head is None
    assert empty_list.tail is None
    assert empty_list._length == 0

def test_push_to_empty_list(empty_list):
    empty_list.push(10)
    assert empty_list.head.data == 10
    assert empty_list.tail.data == 10
    assert empty_list._length == 1

def test_push_to_filled_list(filled_list):
    filled_list.push(4)
    assert filled_list.head.data == 4
    assert filled_list._length == 4

def test_pop_from_empty_list(empty_list):
    with pytest.raises(IndexError):
        empty_list.pop()

def test_pop_from_filled_list(filled_list):
    assert filled_list.pop() == 3
    assert filled_list._length == 2

def test_append_to_empty_list(empty_list):
    empty_list.append(20)
    assert empty_list.tail.data == 20
    assert empty_list.head.data == 20
    assert empty_list._length == 1

def test_append_to_filled_list(filled_list):
    filled_list.append(4)
    assert filled_list.tail.data == 4
    assert filled_list._length == 4

def test_shift_from_empty_list(empty_list):
    with pytest.raises(IndexError):
        empty_list.shift()

def test_shift_from_filled_list(filled_list):
    assert filled_list.shift() == 1
    assert filled_list._length == 2

def test_remove_from_empty_list(empty_list):
    with pytest.raises(ValueError):
        empty_list.remove(5)

def test_remove_nonexistent_value(filled_list):
    with pytest.raises(ValueError):
        filled_list.remove(10)

def test_remove_existing_value(filled_list):
    filled_list.remove(2)
    assert filled_list.head.data == 3
    assert filled_list._length == 2

def test_list_representation(filled_list):
    assert filled_list._repr() == [3, 2, 1]