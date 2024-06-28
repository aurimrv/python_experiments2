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

def test_push(setup_linked_list):
    assert setup_linked_list.head.data == 3
    assert setup_linked_list.head.next.data == 2
    assert setup_linked_list.size() == 3

def test_pop(setup_linked_list):
    assert setup_linked_list.pop() == 3
    assert setup_linked_list.head.data == 2
    assert setup_linked_list.size() == 2

def test_size(setup_linked_list):
    assert setup_linked_list.size() == 3

def test_search(setup_linked_list):
    assert setup_linked_list.search(2).data == 2
    assert setup_linked_list.search(4) is None

def test_remove(setup_linked_list):
    setup_linked_list.remove(2)
    assert setup_linked_list.size() == 2
    assert setup_linked_list.head.next.data == 1

def test_display(setup_linked_list):
    assert setup_linked_list.display() == "(3, 2, 1)"