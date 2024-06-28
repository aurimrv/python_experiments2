# test_linked_list.py

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

def test_push_method():
    ll = LinkedList()
    ll.push(5)
    assert ll.head.data == 5
    assert ll.size() == 1

def test_pop_method(setup_linked_list):
    ll = setup_linked_list
    popped_value = ll.pop()
    assert popped_value == 3
    assert ll.size() == 2

def test_size_method(setup_linked_list):
    ll = setup_linked_list
    assert ll.size() == 3

def test_search_method(setup_linked_list):
    ll = setup_linked_list
    assert ll.search(2).data == 2
    assert ll.search(5) is None

def test_remove_method(setup_linked_list):
    ll = setup_linked_list
    ll.remove(2)
    assert ll.size() == 2
    assert ll.search(2) is None

def test_display_method(setup_linked_list):
    ll = setup_linked_list
    assert ll.display() == '(3, 2, 1)'