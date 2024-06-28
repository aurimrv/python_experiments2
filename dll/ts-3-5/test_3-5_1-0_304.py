import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from dll import Node, DoubleLinkedList

# Test cases for Node class
class TestNode:
    def test_node_initialization(self):
        node = Node(5)
        assert node.data == 5
        assert node.next is None
        assert node.prev is None

    def test_node_representation(self):
        node = Node(10)
        assert repr(node) == "Value: 10"

# Test cases for DoubleLinkedList class
class TestDoubleLinkedList:
    def test_list_initialization(self):
        dll = DoubleLinkedList([1, 2, 3, 4])
        assert dll.head.data == 4
        assert dll.tail.data == 1
        assert dll._length == 4

    def test_push_method(self):
        dll = DoubleLinkedList()
        dll.push(99)
        assert dll.head.data == 99
        assert dll.tail.data == 99
        assert dll._length == 1

    def test_pop_method(self):
        dll = DoubleLinkedList([5])
        result = dll.pop()
        assert result == 5
        assert dll.head is None
        assert dll.tail is None
        assert dll._length == 0

    def test_append_method(self):
        dll = DoubleLinkedList()
        dll.append(77)
        assert dll.head.data == 77
        assert dll.tail.data == 77
        assert dll._length == 1

    def test_shift_method(self):
        dll = DoubleLinkedList([1, 2, 3])
        result = dll.shift()
        assert result == 1
        assert dll.head.data == 3
        assert dll.tail.data == 2
        assert dll._length == 2

    def test_remove_method(self):
        dll = DoubleLinkedList([1, 2, 3, 4, 5])
        dll.remove(3)
        assert dll.head.data == 5
        assert dll.tail.data == 1
        assert dll._length == 4

    def test_remove_not_in_list(self):
        dll = DoubleLinkedList([1, 2, 3])
        with pytest.raises(ValueError):
            dll.remove(5)