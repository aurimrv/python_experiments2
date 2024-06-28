# test_linked_list.py

import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList

@pytest.fixture
def setup_linked_list():
    linked_list = LinkedList()
    return linked_list

def test_push(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(10)
    assert linked_list.size() == 1
    linked_list.push('test')
    assert linked_list.size() == 2

def test_pop(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(10)
    linked_list.push('test')
    assert linked_list.pop() == 'test'
    assert linked_list.pop() == 10

def test_size(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(10)
    linked_list.push('test')
    assert linked_list.size() == 2

def test_search(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(10)
    linked_list.push('test')
    assert linked_list.search(10).data == 10
    assert linked_list.search('test').data == 'test'
    assert linked_list.search(20) is None

def test_remove(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(10)
    linked_list.push('test')
    linked_list.push(20)
    linked_list.remove(10)
    assert linked_list.size() == 2
    linked_list.remove('test')
    assert linked_list.size() == 1

def test_display(setup_linked_list):
    linked_list = setup_linked_list
    linked_list.push(10)
    linked_list.push('test')
    linked_list.push(20)
    assert linked_list.display() == "(20, test, 10)"