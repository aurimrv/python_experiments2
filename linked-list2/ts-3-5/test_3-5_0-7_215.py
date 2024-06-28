import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def setup_linked_list():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    return ll

def test_push():
    ll = LinkedList()
    ll.push(1)
    assert ll.head.data == 1
    assert ll.size() == 1

def test_pop(setup_linked_list):
    ll = setup_linked_list
    assert ll.pop() == 3
    assert ll.size() == 2

def test_size(setup_linked_list):
    ll = setup_linked_list
    assert ll.size() == 3

def test_search(setup_linked_list):
    ll = setup_linked_list
    node = ll.search(2)
    assert node.data == 2

def test_remove(setup_linked_list):
    ll = setup_linked_list
    ll.remove(2)
    assert ll.size() == 2
    assert ll.search(2) is None

def test_display(setup_linked_list):
    ll = setup_linked_list
    assert ll.display() == "(3, 2, 1)"