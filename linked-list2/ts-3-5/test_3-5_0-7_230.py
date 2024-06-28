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

def test_linked_list_init():
    ll = LinkedList()
    assert ll.size() == 0
    assert ll.head is None

def test_linked_list_push():
    ll = LinkedList()
    ll.push(10)
    assert ll.size() == 1
    assert ll.head.data == 10

def test_linked_list_pop():
    ll = LinkedList([5, 10, 15])
    assert ll.pop() == 15
    assert ll.size() == 2

def test_linked_list_search():
    ll = LinkedList([5, 10, 15])
    assert ll.search(10).data == 10
    assert ll.search(20) is None

def test_linked_list_remove():
    ll = LinkedList([5, 10, 15])
    ll.remove(10)
    assert ll.size() == 2
    assert ll.search(10) is None

def test_linked_list_display():
    ll = LinkedList(['a', 'b', 'c'])
    assert ll.display() == '(c, b, a)'