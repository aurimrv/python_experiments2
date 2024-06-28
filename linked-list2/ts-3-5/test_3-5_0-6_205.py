import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

# Test Node class
def test_node_creation():
    node = Node(10)
    assert node.data == 10
    assert node.next is None

# Test LinkedList class
def test_linkedlist_initialization():
    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.size() == 0

def test_linkedlist_push():
    linked_list = LinkedList()
    linked_list.push(20)
    linked_list.push(30)
    assert linked_list.head.data == 30
    assert linked_list.head.next.data == 20
    assert linked_list.size() == 2

def test_linkedlist_pop():
    linked_list = LinkedList()
    linked_list.push(40)
    linked_list.push(50)
    assert linked_list.pop() == 50
    assert linked_list.pop() == 40
    assert linked_list.size() == 0

def test_linkedlist_search():
    linked_list = LinkedList([60, 70, 80])
    assert linked_list.search(70).data == 70
    assert linked_list.search(90) is None

def test_linkedlist_remove():
    linked_list = LinkedList([100, 110, 120])
    linked_list.remove(110)
    assert linked_list.display() == "(120, 100)"
    assert linked_list.size() == 2

def test_linkedlist_display():
    linked_list = LinkedList([130, 140, 150])
    assert linked_list.display() == "(150, 140, 130)"
