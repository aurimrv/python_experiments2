import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

import pytest

@pytest.fixture
def sample_linked_list():
    linked_list = LinkedList()
    return linked_list

def test_push(sample_linked_list):
    sample_linked_list.push(1)
    assert sample_linked_list.head.data == 1
    sample_linked_list.push(2)
    assert sample_linked_list.head.data == 2

def test_pop(sample_linked_list):
    sample_linked_list.push(1)
    sample_linked_list.push(2)
    assert sample_linked_list.pop() == 2
    assert sample_linked_list.head.data == 1

def test_size(sample_linked_list):
    assert sample_linked_list.size() == 0
    sample_linked_list.push(1)
    assert sample_linked_list.size() == 1

def test_search(sample_linked_list):
    sample_linked_list.push(1)
    sample_linked_list.push(2)
    assert sample_linked_list.search(1).data == 1
    assert sample_linked_list.search(2).data == 2

def test_remove(sample_linked_list):
    sample_linked_list.push(1)
    sample_linked_list.push(2)
    sample_linked_list.push(3)
    sample_linked_list.remove(2)
    assert sample_linked_list.size() == 2
    assert sample_linked_list.head.next.data == 1

def test_display(sample_linked_list):
    sample_linked_list.push(1)
    sample_linked_list.push('apple')
    sample_linked_list.push(3.14)
    assert sample_linked_list.display() == '(3.14, apple, 1)'