import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

import pytest

@pytest.fixture
def setup_dll():
    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    return dll

def test_node_repr():
    node = Node(5)
    assert repr(node) == "Value: 5"

def test_dll_push(setup_dll):
    dll = setup_dll
    assert dll.head.data == 3
    assert dll.tail.data == 1
    assert dll._length == 3

def test_dll_pop(setup_dll):
    dll = setup_dll
    assert dll.pop() == 3
    assert dll._length == 2

def test_dll_append(setup_dll):
    dll = setup_dll
    dll.append(4)
    assert dll.tail.data == 4
    assert dll._length == 4

def test_dll_shift(setup_dll):
    dll = setup_dll
    assert dll.shift() == 1
    assert dll._length == 2

def test_dll_remove(setup_dll):
    dll = setup_dll
    dll.remove(2)
    assert dll.head.data == 3
    assert dll._length == 2

def test_dll_remove_not_in_list(setup_dll):
    dll = setup_dll
    with pytest.raises(ValueError):
        dll.remove(5)

def test_dll_repr(setup_dll):
    dll = setup_dll
    assert dll._repr() == [3, 2, 1]