import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def bst():
    return Bst([5, 3, 7, 2, 4, 6, 8])

def test_insert(bst):
    bst.insert(9)
    assert bst.size() == 8
    assert bst.search(9).val == 9

    bst.insert(3)
    assert bst.size() == 8

def test_search(bst):
    assert bst.search(2).val == 2
    assert bst.search(5).val == 5
    assert bst.search(10) is None

def test_size(bst):
    assert bst.size() == 7

def test_depth(bst):
    assert bst.depth() == 3

def test_contains(bst):
    assert bst.contains(4)
    assert not bst.contains(10)

def test_balance(bst):
    assert bst.balance() == 0

def test_pre_order(bst):
    assert list(bst.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(bst):
    assert list(bst.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(bst):
    assert list(bst.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(bst):
    assert list(bst.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

def test_delete(bst):
    bst.delete(2)
    assert not bst.contains(2)
    assert bst.size() == 6

    bst.delete(5)
    assert not bst.contains(5)
    assert bst.size() == 5