import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def sample_linked_list():
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    return ll

def test_push():
    ll = LinkedList()
    ll.push(10)
    assert ll.head.data == 10
    assert ll.size() == 1

def test_pop(sample_linked_list):
    assert sample_linked_list.pop() == 30
    assert sample_linked_list.size() == 2

def test_size(sample_linked_list):
    assert sample_linked_list.size() == 3

def test_search(sample_linked_list):
    assert sample_linked_list.search(20).data == 20
    assert sample_linked_list.search(40) is None

def test_remove(sample_linked_list):
    sample_linked_list.remove(20)
    assert sample_linked_list.size() == 2
    assert sample_linked_list.search(20) is None

def test_display(sample_linked_list):
    assert sample_linked_list.display() == "(30, 20, 10)"