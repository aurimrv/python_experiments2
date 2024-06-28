import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

def test_node_creation():
    node = Node(10)
    assert node.data == 10
    assert node.next is None

def test_linked_list_push():
    ll = LinkedList()
    ll.push(5)
    assert ll.head.data == 5
    assert ll.size() == 1

def test_linked_list_pop():
    ll = LinkedList([1, 2, 3])
    assert ll.pop() == 3
    assert ll.size() == 2

def test_linked_list_size():
    ll = LinkedList([1, 2, 3, 4])
    assert ll.size() == 4

def test_linked_list_search():
    ll = LinkedList([1, 2, 3, 4])
    assert ll.search(3).data == 3
    assert ll.search(5) is None

def test_linked_list_remove():
    ll = LinkedList([1, 2, 3, 4])
    ll.remove(2)
    assert ll.size() == 3
    assert ll.display() == "(4, 3, 1)"

def test_linked_list_display():
    ll = LinkedList([10, 20, 30])
    assert ll.display() == "(30, 20, 10)"