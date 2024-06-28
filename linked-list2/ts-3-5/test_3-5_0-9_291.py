import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

import pytest

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
    popped = ll.pop()
    assert popped == 3
    assert ll.size() == 2

def test_linked_list_size():
    ll = LinkedList([4, 5, 6, 7])
    assert ll.size() == 4

def test_linked_list_search():
    ll = LinkedList([8, 9, 10])
    assert ll.search(8).data == 8
    assert ll.search(11) is None

def test_linked_list_remove():
    ll = LinkedList([11, 12, 13])
    ll.remove(11)
    assert ll.size() == 2
    assert ll.head.data == 13

def test_linked_list_display():
    ll = LinkedList([14, 15, 16])
    assert ll.display() == "(16, 15, 14)"