import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

import pytest

@pytest.fixture
def sample_linked_list():
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    return ll

def test_push():
    ll = LinkedList()
    ll.push(5)
    assert ll.head.data == 5

def test_pop(sample_linked_list):
    assert sample_linked_list.pop() == 3
    assert sample_linked_list.pop() == 2

def test_size(sample_linked_list):
    assert sample_linked_list.size() == 3

def test_search(sample_linked_list):
    assert sample_linked_list.search(2).data == 2
    assert sample_linked_list.search(5) is None

def test_remove(sample_linked_list):
    sample_linked_list.remove(2)
    assert sample_linked_list.size() == 2
    assert sample_linked_list.search(2) is None

def test_display(sample_linked_list):
    assert sample_linked_list.display() == '(3, 2, 1)'