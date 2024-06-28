import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

def test_node():
    node = Node('data')
    assert node.data == 'data'
    assert node.next is None

def test_linkedlist_push():
    ll = LinkedList()
    ll.push(1)
    assert ll.head.data == 1
    assert ll.head.next is None

def test_linkedlist_push_multiple_elements():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    assert ll.head.data == 3
    assert ll.head.next.data == 2

def test_linkedlist_pop():
    ll = LinkedList()
    ll.push(1)
    assert ll.pop() == 1
    assert ll.head is None

def test_linkedlist_size():
    ll = LinkedList()
    assert ll.size() == 0
    ll.push(1)
    ll.push(2)
    assert ll.size() == 2

def test_linkedlist_search():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    assert ll.search(1).data == 1
    assert ll.search(3) is None

def test_linkedlist_remove():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.remove(1)
    assert ll.display() == '(2)'

def test_linkedlist_display():
    ll = LinkedList()
    ll.push(1)
    ll.push('test')
    ll.push(3)
    assert ll.display() == '(3, test, 1)'    