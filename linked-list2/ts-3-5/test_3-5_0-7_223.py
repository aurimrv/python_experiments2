import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

def test_node_creation():
    node = Node(5)
    assert node.data == 5
    assert node.next is None

def test_node_with_next():
    next_node = Node(10)
    node = Node(5, next_node)
    assert node.data == 5
    assert node.next == next_node

def test_linked_list_initialization():
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.size() == 3

def test_linked_list_push():
    linked_list = LinkedList()
    linked_list.push(10)
    linked_list.push(20)
    assert linked_list.size() == 2

def test_linked_list_pop():
    linked_list = LinkedList([1, 2, 3])
    popped_value = linked_list.pop()
    assert popped_value == 3
    assert linked_list.size() == 2

def test_linked_list_search():
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.search(2).data == 2

def test_linked_list_remove():
    linked_list = LinkedList([1, 2, 3])
    linked_list.remove(2)
    assert linked_list.size() == 2
    assert linked_list.search(2) is None

def test_linked_list_display():
    linked_list = LinkedList([1, 'abc', 3.14])
    assert linked_list.display() == "(3.14, abc, 1)"