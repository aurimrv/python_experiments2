import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def sample_linked_list():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    return linked_list

def test_push():
    linked_list = LinkedList()
    linked_list.push(1)
    assert linked_list.head.data == 1
    assert linked_list.size() == 1

def test_pop(sample_linked_list):
    popped_value = sample_linked_list.pop()
    assert popped_value == 3
    assert sample_linked_list.size() == 2

def test_size(sample_linked_list):
    assert sample_linked_list.size() == 3

def test_search(sample_linked_list):
    assert sample_linked_list.search(2).data == 2
    assert sample_linked_list.search(4) is None

def test_remove(sample_linked_list):
    sample_linked_list.remove(2)
    assert sample_linked_list.size() == 2
    assert sample_linked_list.search(2) is None

def test_display(sample_linked_list):
    assert sample_linked_list.display() == "(3, 2, 1)"