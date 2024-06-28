import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

import pytest

@pytest.fixture
def init_empty_dll():
    return DoubleLinkedList()

@pytest.fixture
def init_dll_with_data():
    return DoubleLinkedList([1, 2, 3, 4])

def test_node_init():
    n = Node(5)
    assert n.data == 5
    assert n.prev is None
    assert n.next is None

def test_dll_init_empty(init_empty_dll):
    assert init_empty_dll.head is None
    assert init_empty_dll.tail is None
    assert init_empty_dll._length == 0

def test_dll_init_with_data(init_dll_with_data):
    assert init_dll_with_data.head.data == 4
    assert init_dll_with_data.tail.data == 1
    assert init_dll_with_data._length == 4

def test_dll_push(init_empty_dll):
    init_empty_dll.push(10)
    assert init_empty_dll.head.data == 10
    assert init_empty_dll.tail.data == 10
    assert init_empty_dll._length == 1

    init_empty_dll.push(20)
    assert init_empty_dll.head.data == 20
    assert init_empty_dll.tail.data == 10
    assert init_empty_dll._length == 2

def test_dll_pop(init_dll_with_data):
    assert init_dll_with_data.pop() == 4
    assert init_dll_with_data.head.data == 3
    assert init_dll_with_data.tail.data == 1
    assert init_dll_with_data._length == 3

    assert init_dll_with_data.pop() == 3
    assert init_dll_with_data.head.data == 2
    assert init_dll_with_data.tail.data == 1
    assert init_dll_with_data._length == 2

def test_dll_append(init_empty_dll):
    init_empty_dll.append(15)
    assert init_empty_dll.head.data == 15
    assert init_empty_dll.tail.data == 15
    assert init_empty_dll._length == 1

    init_empty_dll.append(25)
    assert init_empty_dll.head.data == 15
    assert init_empty_dll.tail.data == 25
    assert init_empty_dll._length == 2

def test_dll_shift(init_dll_with_data):
    assert init_dll_with_data.shift() == 1
    assert init_dll_with_data.head.data == 4
    assert init_dll_with_data.tail.data == 2
    assert init_dll_with_data._length == 3

    assert init_dll_with_data.shift() == 2
    assert init_dll_with_data.head.data == 4
    assert init_dll_with_data.tail.data == 3
    assert init_dll_with_data._length == 2

def test_dll_remove(init_dll_with_data):
    init_dll_with_data.remove(3)
    assert init_dll_with_data.head.data == 4
    assert init_dll_with_data.tail.data == 1
    assert init_dll_with_data._length == 3

    with pytest.raises(ValueError):
        init_dll_with_data.remove(5)