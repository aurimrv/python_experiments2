import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def test_linked_list():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    return linked_list

def test_push(test_linked_list):
    assert test_linked_list.head.data == 3
    assert test_linked_list.size() == 3
    test_linked_list.push(4)
    assert test_linked_list.head.data == 4
    assert test_linked_list.size() == 4

def test_pop(test_linked_list):
    popped_value = test_linked_list.pop()
    assert popped_value == 3
    assert test_linked_list.size() == 2
    popped_value = test_linked_list.pop()
    assert popped_value == 2
    assert test_linked_list.size() == 1

def test_size(test_linked_list):
    assert test_linked_list.size() == 3
    test_linked_list.push(4)
    assert test_linked_list.size() == 4

def test_search(test_linked_list):
    assert test_linked_list.search(2).data == 2
    assert test_linked_list.search(5) is None

def test_remove(test_linked_list):
    test_linked_list.remove(2)
    assert test_linked_list.size() == 2
    test_linked_list.remove(3)
    assert test_linked_list.size() == 1
    test_linked_list.remove(1)
    assert test_linked_list.size() == 0

def test_display(test_linked_list):
    assert test_linked_list.display() == '(3, 2, 1)'
    test_linked_list.remove(3)
    assert test_linked_list.display() == '(2, 1)'
    test_linked_list.remove(1)
    assert test_linked_list.display() == '(2)'