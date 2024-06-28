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
    ll.push(10)
    ll.push(20)
    ll.push(30)
    return ll

def test_push():
    ll = LinkedList()
    ll.push(10)
    assert ll.head.data == 10
    assert ll.size() == 1

def test_pop(setup_linked_list):
    ll = setup_linked_list
    data = ll.pop()
    assert data == 30
    assert ll.size() == 2

def test_size(setup_linked_list):
    ll = setup_linked_list
    assert ll.size() == 3

def test_search(setup_linked_list):
    ll = setup_linked_list
    node = ll.search(20)
    assert node.data == 20

def test_search_not_found(setup_linked_list):
    ll = setup_linked_list
    node = ll.search(40)
    assert node == None

def test_remove(setup_linked_list):
    ll = setup_linked_list
    ll.remove(20)
    assert ll.size() == 2
    assert ll.display() == "(30, 10)"

def test_display(setup_linked_list):
    ll = setup_linked_list
    display_str = ll.display()
    assert display_str == "(30, 20, 10)"