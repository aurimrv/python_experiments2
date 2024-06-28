import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def sample_linked_list():
    llist = LinkedList([1, 2, 3, 4])
    return llist

def test_push(sample_linked_list):
    assert sample_linked_list.size() == 4
    sample_linked_list.push(5)
    assert sample_linked_list.size() == 5

def test_pop(sample_linked_list):
    assert sample_linked_list.pop() == 4
    assert sample_linked_list.size() == 3

def test_size(sample_linked_list):
    assert sample_linked_list.size() == 4
    sample_linked_list.push(5)
    assert sample_linked_list.size() == 5

def test_search(sample_linked_list):
    node = sample_linked_list.search(3)
    assert node.data == 3
    non_existing_node = sample_linked_list.search(10)
    assert non_existing_node is None

def test_remove(sample_linked_list):
    sample_linked_list.remove(2)
    assert sample_linked_list.size() == 3

def test_display(sample_linked_list):
    assert sample_linked_list.display() == '(4, 3, 2, 1)'