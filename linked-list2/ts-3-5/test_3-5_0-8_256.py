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
    return linked_list

def test_push(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(1)
    assert linked_list.head.data == 1
    linked_list.push(2)
    assert linked_list.head.data == 2

def test_pop(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(1)
    linked_list.push(2)
    popped_value = linked_list.pop()
    assert popped_value == 2
    assert linked_list.head.data == 1

def test_size(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(1)
    linked_list.push(2)
    assert linked_list.size() == 2

def test_search(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(1)
    linked_list.push(2)
    assert linked_list.search(2).data == 2
    assert linked_list.search(3) is None

def test_remove(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.remove(2)
    assert linked_list.size() == 2
    assert linked_list.head.next.data == 1

def test_display(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(1)
    linked_list.push('test')
    linked_list.push(3.5)
    assert linked_list.display() == '(3.5, test, 1)'