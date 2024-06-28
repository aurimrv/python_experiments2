import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

# Test cases for Node class
def test_node_creation():
    node = Node(5)
    assert node.data == 5
    assert node.next == None

# Test cases for LinkedList class
def test_linked_list_empty():
    linked_list = LinkedList()
    assert linked_list.size() == 0

def test_linked_list_push_pop():
    linked_list = LinkedList()
    linked_list.push(1)
    assert linked_list.pop() == 1

def test_linked_list_push_multiple():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.display() == '(3, 2, 1)'

def test_linked_list_search():
    linked_list = LinkedList([1, 2, 3, 4, 5])
    node = linked_list.search(3)
    assert node.data == 3

def test_linked_list_remove():
    linked_list = LinkedList([1, 2, 3, 4, 5])
    node = linked_list.search(3)
    linked_list.remove(node.data)
    assert linked_list.size() == 4

def test_linked_list_display():
    linked_list = LinkedList([12, 'sam', 37, 'tango'])
    assert linked_list.display() == '(tango, 37, sam, 12)'