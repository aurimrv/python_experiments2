import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

import pytest

@pytest.fixture
def empty_dll():
    return DoubleLinkedList()

@pytest.fixture
def filled_dll():
    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    return dll

def test_empty_dll_initialization(empty_dll):
    assert empty_dll.head is None
    assert empty_dll.tail is None
    assert empty_dll._length == 0

def test_filled_dll_initialization(filled_dll):
    assert filled_dll.head.data == 3
    assert filled_dll.tail.data == 1
    assert filled_dll._length == 3

def test_push_method(empty_dll):
    empty_dll.push(5)
    assert empty_dll.head.data == 5
    assert empty_dll.tail.data == 5
    assert empty_dll._length == 1

def test_pop_method(filled_dll):
    assert filled_dll.pop() == 3
    assert filled_dll.pop() == 2
    assert filled_dll.pop() == 1
    assert filled_dll._length == 0

def test_append_method(empty_dll):
    empty_dll.append(10)
    assert empty_dll.head.data == 10
    assert empty_dll.tail.data == 10
    assert empty_dll._length == 1

def test_shift_method(filled_dll):
    assert filled_dll.shift() == 1
    assert filled_dll.shift() == 2
    assert filled_dll.shift() == 3
    assert filled_dll._length == 0

def test_remove_method(filled_dll):
    filled_dll.remove(2)
    assert filled_dll.head.data == 3
    assert filled_dll.tail.data == 1
    assert filled_dll._length == 2

    filled_dll.remove(3)
    assert filled_dll.head.data == 1
    assert filled_dll.tail.data == 1
    assert filled_dll._length == 1

def test_remove_method_non_existent(filled_dll):
    with pytest.raises(ValueError):
        filled_dll.remove(5)