import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

import pytest

def test_node_creation():
    node = Node(5)
    assert node.data == 5
    assert node.next is None

def test_linked_list_initialization():
    lst = LinkedList()
    assert lst.size() == 0
    assert lst.head is None

def test_linked_list_push():
    lst = LinkedList()
    lst.push(10)
    assert lst.size() == 1
    assert lst.head.data == 10

def test_linked_list_pop():
    lst = LinkedList([1, 2, 3])
    popped_val = lst.pop()
    assert popped_val == 3
    assert lst.size() == 2

def test_linked_list_search():
    lst = LinkedList([1, 2, 3])
    found_node = lst.search(2)
    assert found_node.data == 2

def test_linked_list_remove():
    lst = LinkedList([1, 2, 3])
    lst.remove(2)
    assert lst.size() == 2
    found_node = lst.search(2)
    assert found_node is None

def test_linked_list_display():
    lst = LinkedList(['a', 'b', 'c'])
    display_str = lst.display()
    assert display_str == "(c, b, a)"