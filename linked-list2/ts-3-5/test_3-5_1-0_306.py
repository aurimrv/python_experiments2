import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

# Test cases for Node class
def test_node_creation():
    n = Node(5)
    assert n.data == 5
    assert n.next is None

def test_node_next_node():
    n1 = Node(10)
    n2 = Node(20, n1)
    assert n2.next == n1


# Test cases for LinkedList class
def test_linked_list_creation_empty():
    ll = LinkedList()
    assert ll.head is None
    assert ll.size() == 0

def test_linked_list_creation_single_value():
    ll = LinkedList(5)
    assert ll.head.data == 5
    assert ll.size() == 1

def test_push():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    assert ll.head.data == 2
    assert ll.head.next.data == 1
    assert ll.size() == 2

def test_pop():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    assert ll.pop() == 2
    assert ll.size() == 1
    assert ll.pop() == 1
    assert ll.size() == 0

def test_size():
    ll = LinkedList()
    assert ll.size() == 0
    ll.push(5)
    assert ll.size() == 1

def test_search():
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    assert ll.search(20).data == 20
    assert ll.search(40) is None

def test_remove():
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.remove(20)
    assert ll.size() == 2
    assert ll.display() == "(30, 10)"

def test_display():
    ll = LinkedList()
    ll.push(12)
    ll.push('sam')
    ll.push(37)
    ll.push('tango')
    assert ll.display() == "(tango, 37, sam, 12)"