import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

# Test cases for Node class
def test_node_init():
    node = Node(10)
    assert node.data == 10
    assert node.next is None

def test_node_init_with_next():
    next_node = Node(20)
    node = Node(10, next_node)
    assert node.data == 10
    assert node.next == next_node

# Test cases for LinkedList class
def test_linkedlist_init():
    ll = LinkedList()
    assert ll.head is None
    assert ll._length == 0

def test_linkedlist_push():
    ll = LinkedList()
    ll.push(10)
    assert ll.head.data == 10
    assert ll._length == 1

def test_linkedlist_push_multiple():
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    assert ll.head.data == 20
    assert ll.head.next.data == 10
    assert ll._length == 2

def test_linkedlist_pop():
    ll = LinkedList()
    ll.push(10)
    assert ll.pop() == 10
    assert ll.head is None
    assert ll._length == 0

def test_linkedlist_size():
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    assert ll.size() == 2

def test_linkedlist_search():
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    assert ll.search(10).data == 10

def test_linkedlist_search_not_found():
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    assert ll.search(30) is None

def test_linkedlist_remove():
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    ll.remove(10)
    assert ll.size() == 1
    assert ll.head.data == 20

def test_linkedlist_display():
    ll = LinkedList()
    ll.push(10)
    ll.push('hello')
    ll.push(30)
    assert ll.display() == '(30, hello, 10)'
