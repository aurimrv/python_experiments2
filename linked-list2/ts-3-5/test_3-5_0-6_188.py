import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

import pytest

@pytest.fixture
def setup_linked_list():
    ll = LinkedList()
    ll.push(5)
    ll.push(10)
    ll.push(15)
    ll.push(20)
    return ll

def test_push(setup_linked_list):
    assert setup_linked_list.head.data == 20
    assert setup_linked_list.head.next.data == 15

def test_pop(setup_linked_list):
    assert setup_linked_list.pop() == 20
    assert setup_linked_list.head.data == 15

def test_size(setup_linked_list):
    assert setup_linked_list.size() == 4

def test_search(setup_linked_list):
    assert setup_linked_list.search(10).data == 10
    assert setup_linked_list.search(100) is None

def test_remove(setup_linked_list):
    setup_linked_list.remove(15)
    assert setup_linked_list.size() == 3
    assert setup_linked_list.head.next.data == 10

def test_display(setup_linked_list):
    assert setup_linked_list.display() == "(20, 15, 10, 5)"