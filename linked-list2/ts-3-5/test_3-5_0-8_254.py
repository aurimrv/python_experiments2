import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def sample_linked_list():
    # Fixture to create a sample linked list for testing
    ll = LinkedList()
    ll.push(1)
    ll.push('hello')
    ll.push(3.14)
    return ll

def test_push(sample_linked_list):
    sample_linked_list.push('new_value')
    assert sample_linked_list.head.data == 'new_value'
    assert sample_linked_list.size() == 4

def test_pop(sample_linked_list):
    popped_value = sample_linked_list.pop()
    assert popped_value == 3.14
    assert sample_linked_list.size() == 2

def test_size(sample_linked_list):
    assert sample_linked_list.size() == 3

def test_search(sample_linked_list):
    assert sample_linked_list.search(1).data == 1
    assert sample_linked_list.search('hello').data == 'hello'
    assert sample_linked_list.search(3.14).data == 3.14
    assert sample_linked_list.search('random') is None

def test_remove(sample_linked_list):
    sample_linked_list.remove(1)
    assert sample_linked_list.size() == 2
    sample_linked_list.remove('hello')
    assert sample_linked_list.size() == 1
    sample_linked_list.remove(3.14)
    assert sample_linked_list.size() == 0

def test_display(sample_linked_list):
    assert sample_linked_list.display() == "(3.14, hello, 1)"
