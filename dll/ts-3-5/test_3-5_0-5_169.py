import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

@pytest.fixture
def empty_list():
    return DoubleLinkedList()

@pytest.fixture
def sample_list():
    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    return dll

def test_push(empty_list, sample_list):
    empty_list.push(5)
    assert empty_list.head.data == 5
    assert empty_list.tail.data == 5

    sample_list.push(10)
    assert sample_list.head.data == 10
    assert sample_list.tail.data == 1

def test_pop(sample_list):
    assert sample_list.pop() == 3
    assert sample_list.pop() == 2
    assert sample_list.pop() == 1

    with pytest.raises(IndexError):
        sample_list.pop()

def test_append(empty_list, sample_list):
    empty_list.append(8)
    assert empty_list.head.data == 8
    assert empty_list.tail.data == 8

    sample_list.append(15)
    assert sample_list.head.data == 3
    assert sample_list.tail.data == 15

def test_shift(sample_list):
    assert sample_list.shift() == 1
    assert sample_list.shift() == 2
    assert sample_list.shift() == 3

    with pytest.raises(IndexError):
        sample_list.shift()

def test_remove(sample_list):
    sample_list.remove(2)
    assert sample_list.head.data == 3
    assert sample_list.tail.data == 1

    with pytest.raises(ValueError):
        sample_list.remove(5)

def test_initialization():
    dll = DoubleLinkedList([1, 2, 3])
    assert dll.head.data == 3
    assert dll.tail.data == 1
    assert dll._length == 3

    empty_dll = DoubleLinkedList()
    assert empty_dll.head == None
    assert empty_dll.tail == None
    assert empty_dll._length == 0