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

def test_linked_list_push():
    ll = LinkedList()
    ll.push(5)
    assert ll.head.data == 5
    assert ll.size() == 1

def test_linked_list_pop():
    ll = LinkedList([5, 10, 15])
    popped_value = ll.pop()
    assert popped_value == 15
    assert ll.size() == 2

def test_linked_list_size():
    ll = LinkedList([5, 10, 15])
    assert ll.size() == 3

def test_linked_list_search_found():
    ll = LinkedList([5, 10, 15])
    node = ll.search(10)
    assert node.data == 10

def test_linked_list_search_not_found():
    ll = LinkedList([5, 10, 15])
    node = ll.search(20)
    assert node is None

def test_linked_list_remove():
    ll = LinkedList([5, 10, 15])
    ll.remove(10)
    assert ll.size() == 2
    assert ll.display() == "(15, 5)"

def test_linked_list_display():
    ll = LinkedList([5, 'test', 10])
    assert ll.display() == "(10, test, 5)"