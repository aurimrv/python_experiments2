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
    ll.push(10)
    ll.push('apple')
    ll.push(20)
    ll.push('banana')
    return ll

def test_push():
    ll = LinkedList()
    ll.push(5)
    assert ll.head.data == 5
    assert ll.size() == 1

def test_pop():
    ll = LinkedList()
    ll.push(100)
    result = ll.pop()
    assert result == 100
    assert ll.size() == 0

def test_size():
    ll = LinkedList()
    assert ll.size() == 0
    ll.push(1)
    ll.push(2)
    assert ll.size() == 2

def test_search_found(sample_linked_list):
    assert sample_linked_list.search('apple').data == 'apple'

def test_search_not_found(sample_linked_list):
    assert sample_linked_list.search('grape') is None

def test_remove_head(sample_linked_list):
    sample_linked_list.remove(10)
    assert sample_linked_list.size() == 3
    assert sample_linked_list.head.data != 10

def test_remove_middle(sample_linked_list):
    sample_linked_list.remove('apple')
    assert sample_linked_list.size() == 3
    assert sample_linked_list.search('apple') is None

def test_remove_last(sample_linked_list):
    sample_linked_list.remove('banana')
    assert sample_linked_list.size() == 3
    assert sample_linked_list.search('banana') is None

def test_display(sample_linked_list):
    display_str = sample_linked_list.display()
    assert display_str == "(banana, 20, apple, 10)"