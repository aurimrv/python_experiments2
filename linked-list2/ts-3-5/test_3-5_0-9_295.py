import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

# Test for Node class
def test_node_creation():
    data = 10
    n = Node(data)
    assert n.data == data
    assert n.next is None

# Test for LinkedList class
def test_linked_list_initialization():
    data = [1, 2, 3, 4]
    ll = LinkedList(data)
    assert ll.size() == 4
    assert ll.display() == "(4, 3, 2, 1)"

def test_linked_list_push():
    ll = LinkedList()
    ll.push(5)
    assert ll.size() == 1
    assert ll.display() == "(5)"

def test_linked_list_pop():
    ll = LinkedList([1, 2, 3])
    popped_val = ll.pop()
    assert popped_val == 3
    assert ll.size() == 2
    assert ll.display() == "(2, 1)"

def test_linked_list_search():
    ll = LinkedList([10, 20, 30, 40])
    found_node = ll.search(20)
    assert found_node.data == 20

def test_linked_list_remove():
    ll = LinkedList([1, 2, 3, 4])
    ll.remove(2)
    assert ll.size() == 3
    assert ll.display() == "(4, 3, 1)"
    ll.remove(4)
    assert ll.size() == 2
    assert ll.display() == "(3, 1)"

# Additional test for edge cases

def test_linked_list_pop_empty_list():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.pop()

def test_linked_list_search_not_found():
    ll = LinkedList([1, 2, 3, 4])
    found_node = ll.search(5)
    assert found_node is None
