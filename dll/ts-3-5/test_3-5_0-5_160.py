import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

import pytest

@pytest.fixture
def sample_list():
    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    return dll

def test_node_init():
    node = Node(5)
    assert node.data == 5
    assert node.next is None
    assert node.prev is None

def test_dll_init_empty():
    dll = DoubleLinkedList()
    assert dll.head is None
    assert dll.tail is None
    assert dll._length == 0

def test_dll_init_with_data():
    dll = DoubleLinkedList([1, 2, 3])
    assert dll.head.data == 3
    assert dll.tail.data == 1
    assert dll._length == 3

def test_push(sample_list):
    sample_list.push(4)
    assert sample_list.head.data == 4
    assert sample_list.head.next.data == 3

def test_pop(sample_list):
    assert sample_list.pop() == 3
    assert sample_list.head.data == 2

def test_append(sample_list):
    sample_list.append(0)
    assert sample_list.tail.data == 0
    assert sample_list.tail.prev.data == 1

def test_shift(sample_list):
    assert sample_list.shift() == 1
    assert sample_list.tail.data == 2

def test_remove(sample_list):
    sample_list.remove(2)
    assert sample_list.head.data == 3
    assert sample_list.tail.data == 1

def test_remove_not_in_list(sample_list):
    with pytest.raises(ValueError):
        sample_list.remove(5)

def test_remove_single_element():
    dll = DoubleLinkedList(5)
    dll.remove(5)
    assert dll.head is None
    assert dll.tail is None
    assert dll._length == 0