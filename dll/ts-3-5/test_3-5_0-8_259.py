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
    dll.append(3)
    return dll

def test_empty_list_creation(empty_list):
    assert empty_list.head is None
    assert empty_list.tail is None
    assert empty_list._length == 0

def test_filled_list_creation(filled_list):
    assert filled_list.head.data == 2
    assert filled_list.tail.data == 3
    assert filled_list._length == 3

def test_push_method(empty_list):
    empty_list.push(5)
    assert empty_list.head.data == 5

def test_pop_method(filled_list):
    assert filled_list.pop() == 2
    assert filled_list.head.data == 1

def test_append_method(empty_list):
    empty_list.append(10)
    assert empty_list.tail.data == 10

def test_shift_method(filled_list):
    assert filled_list.shift() == 3
    assert filled_list.tail.data == 1

def test_remove_method(filled_list):
    filled_list.remove(2)
    assert filled_list.head.data == 1
    assert filled_list._length == 2
    with pytest.raises(ValueError):
        filled_list.remove(5)

def test_remove_method_single_element(empty_list):
    empty_list.push(99)
    empty_list.remove(99)
    assert empty_list.head is None
    assert empty_list.tail is None
    assert empty_list._length == 0