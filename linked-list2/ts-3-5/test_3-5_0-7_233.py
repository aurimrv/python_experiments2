import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from linked_list2 import Node, LinkedList


@pytest.fixture
def setup_linked_list():
    ll = LinkedList()
    return ll


def test_push(setup_linked_list):
    ll = setup_linked_list
    ll.push(10)
    assert ll.head.data == 10
    ll.push(20)
    assert ll.head.data == 20
    assert ll.head.next.data == 10


def test_pop(setup_linked_list):
    ll = setup_linked_list
    ll.push(10)
    ll.push(20)
    assert ll.pop() == 20
    assert ll.pop() == 10
    with pytest.raises(IndexError):
        ll.pop()


def test_size(setup_linked_list):
    ll = setup_linked_list
    assert ll.size() == 0
    ll.push(10)
    ll.push(20)
    assert ll.size() == 2
    ll.pop()
    assert ll.size() == 1


def test_search(setup_linked_list):
    ll = setup_linked_list
    ll.push(10)
    ll.push(20)
    assert ll.search(10).data == 10
    assert ll.search(20).data == 20
    assert ll.search(30) is None


def test_remove(setup_linked_list):
    ll = setup_linked_list
    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.remove(20)
    assert ll.head.data == 30
    assert ll.head.next.data == 10
    assert ll.size() == 2
    ll.remove(30)
    assert ll.head.data == 10
    assert ll.size() == 1
    ll.remove(10)
    assert ll.head is None
    assert ll.size() == 0


def test_display(setup_linked_list):
    ll = setup_linked_list
    ll.push(10)
    ll.push("hello")
    ll.push(30)
    assert ll.display() == "(30, hello, 10)"