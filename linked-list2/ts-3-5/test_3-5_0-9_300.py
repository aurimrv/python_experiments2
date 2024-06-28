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

def test_push():
    ll = LinkedList()
    ll.push(10)
    assert ll.size() == 1
    assert ll.head.data == 10

def test_pop():
    ll = LinkedList([1, 2, 3])
    popped_value = ll.pop()
    assert popped_value == 3
    assert ll.size() == 2

def test_size():
    ll = LinkedList([1, 2, 3, 4])
    assert ll.size() == 4

def test_search():
    ll = LinkedList([1, 2, 3])
    assert ll.search(2).data == 2
    assert ll.search(4) is None

def test_remove():
    ll = LinkedList([1, 2, 3, 4, 5])
    ll.remove(3)
    assert ll.size() == 4
    assert ll.display() == "(5, 4, 2, 1)"

def test_display():
    ll = LinkedList([10, "foo", 20])
    assert ll.display() == "(20, foo, 10)"