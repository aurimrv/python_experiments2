import os
import sys
import pytest
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def create_linked_list():
    ll = LinkedList()
    ll.push('apple')
    ll.push('banana')
    ll.push('cherry')
    return ll

def test_push(create_linked_list):
    assert create_linked_list.head.data == 'cherry'
    assert create_linked_list.size() == 3

def test_pop(create_linked_list):
    assert create_linked_list.pop() == 'cherry'
    assert create_linked_list.size() == 2

def test_size(create_linked_list):
    assert create_linked_list.size() == 3

def test_search(create_linked_list):
    assert create_linked_list.search('banana').data == 'banana'
    assert create_linked_list.search('grape') is None

def test_remove(create_linked_list):
    create_linked_list.remove('banana')
    assert create_linked_list.size() == 2
    create_linked_list.remove('apple')
    assert create_linked_list.size() == 1
    create_linked_list.remove('cherry')
    assert create_linked_list.size() == 0

def test_display(create_linked_list):
    assert create_linked_list.display() == "(cherry, banana, apple)"