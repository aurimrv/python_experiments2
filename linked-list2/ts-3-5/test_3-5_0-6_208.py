import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def create_linked_list():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    return linked_list

def test_push(create_linked_list):
    assert create_linked_list.head.data == 3
    assert create_linked_list.size() == 3

def test_pop(create_linked_list):
    assert create_linked_list.pop() == 3
    assert create_linked_list.size() == 2

def test_size(create_linked_list):
    assert create_linked_list.size() == 3

def test_search(create_linked_list):
    assert create_linked_list.search(2).data == 2
    assert create_linked_list.search(4) == None

def test_remove(create_linked_list):
    create_linked_list.remove(2)
    assert create_linked_list.size() == 2
    assert create_linked_list.search(2) == None

def test_display(create_linked_list):
    assert create_linked_list.display() == "(3, 2, 1)"