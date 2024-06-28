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
    dll.append(4)
    dll.append(5)
    return dll

def test_node_repr():
    node = Node(10)
    assert repr(node) == "Value: 10"

def test_dll_push(empty_list):
    empty_list.push(100)
    assert empty_list.head.data == 100
    assert empty_list.tail.data == 100

def test_dll_pop(filled_list):
    assert filled_list.pop() == 3
    assert filled_list.pop() == 2

def test_dll_append(empty_list):
    empty_list.append(200)
    assert empty_list.head.data == 200
    assert empty_list.tail.data == 200

def test_dll_shift(filled_list):
    assert filled_list.shift() == 5
    assert filled_list.shift() == 4

def test_dll_remove(filled_list):
    filled_list.remove(2)
    assert filled_list._repr() == [3, 1, 4, 5]

def test_dll_remove_nonexistent(filled_list):
    with pytest.raises(ValueError):
        filled_list.remove(10)