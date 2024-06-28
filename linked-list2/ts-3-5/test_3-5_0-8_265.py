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
    ll.push('two')
    ll.push(3.0)
    return ll

def test_linkedlist_push():
    ll = LinkedList()
    ll.push(1)
    assert ll.size() == 1
    ll.push('test')
    assert ll.size() == 2

def test_linkedlist_pop(sample_linked_list):
    assert sample_linked_list.pop() == 3.0
    assert sample_linked_list.size() == 2
    assert sample_linked_list.pop() == 'two'
    assert sample_linked_list.size() == 1

def test_linkedlist_size(sample_linked_list):
    assert sample_linked_list.size() == 3
    sample_linked_list.pop()
    assert sample_linked_list.size() == 2

def test_linkedlist_search(sample_linked_list):
    assert sample_linked_list.search('two').data == 'two'
    assert sample_linked_list.search(5) is None

def test_linkedlist_remove(sample_linked_list):
    node_to_remove = sample_linked_list.search('two')
    sample_linked_list.remove(node_to_remove.data)
    assert sample_linked_list.size() == 2
    assert sample_linked_list.search('two') is None

def test_linkedlist_display(sample_linked_list):
    assert sample_linked_list.display() == '(3.0, two, 1)'