import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

@pytest.fixture
def sample_list():
    return DoubleLinkedList([1, 2, 3, 4, 5])

def test_node_repr():
    node = Node(10)
    assert repr(node) == "Value: 10"

def test_push(sample_list):
    sample_list.push(0)
    assert sample_list.head.data == 0

def test_pop(sample_list):
    assert sample_list.pop() == 5

def test_append(sample_list):
    sample_list.append(6)
    assert sample_list.tail.data == 6

def test_shift(sample_list):
    assert sample_list.shift() == 1

def test_remove(sample_list):
    sample_list.remove(3)
    assert sample_list._repr() == [5, 4, 2, 1]

def test_remove_nonexistent(sample_list):
    with pytest.raises(ValueError):
        sample_list.remove(10)

def test_initialization():
    dll = DoubleLinkedList()
    assert dll.head is None
    assert dll.tail is None
    assert dll._length == 0

def test_single_value_push():
    dll = DoubleLinkedList(10)
    assert dll.head.data == 10
    assert dll.tail.data == 10
    assert dll._length == 1