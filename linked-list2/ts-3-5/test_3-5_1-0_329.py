import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def sample_linked_list():
    return LinkedList([1, 2, 3, 4, 5])

def test_push(sample_linked_list):
    sample_linked_list.push(6)
    assert sample_linked_list.size() == 6
    assert sample_linked_list.head.data == 6

def test_pop(sample_linked_list):
    popped_value = sample_linked_list.pop()
    assert popped_value == 5
    assert sample_linked_list.size() == 4

def test_size(sample_linked_list):
    assert sample_linked_list.size() == 5

def test_search(sample_linked_list):
    assert sample_linked_list.search(3).data == 3

def test_remove(sample_linked_list):
    sample_linked_list.remove(3)
    assert sample_linked_list.size() == 4
    assert sample_linked_list.search(3) is None

def test_display(sample_linked_list):
    assert sample_linked_list.display() == "(5, 4, 3, 2, 1)"