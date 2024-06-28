import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def setup_linked_list():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    return linked_list

# Test cases for Node class
def test_node_creation():
    node = Node(5)
    assert node.data == 5
    assert node.next is None

# Test cases for LinkedList class
def test_linked_list_creation():
    linked_list = LinkedList()
    assert linked_list.size() == 0
    assert linked_list.head is None

def test_linked_list_push(setup_linked_list):
    assert setup_linked_list.size() == 3
    assert setup_linked_list.head.data == 3

def test_linked_list_pop(setup_linked_list):
    assert setup_linked_list.pop() == 3
    assert setup_linked_list.size() == 2

def test_linked_list_size(setup_linked_list):
    assert setup_linked_list.size() == 3

def test_linked_list_search(setup_linked_list):
    assert setup_linked_list.search(2).data == 2
    assert setup_linked_list.search(5) is None

def test_linked_list_remove(setup_linked_list):
    setup_linked_list.remove(2)
    assert setup_linked_list.size() == 2
    assert setup_linked_list.search(2) is None

def test_linked_list_display(setup_linked_list):
    assert setup_linked_list.display() == '(3, 2, 1)'