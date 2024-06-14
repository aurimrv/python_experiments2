import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def bst():
    return Bst([5, 3, 8, 2, 4, 7, 10])

def test_insert(bst):
    bst.insert(9)
    assert bst.contains(9)

def test_search(bst):
    assert bst.search(8).val == 8

def test_size(bst):
    assert bst.size() == 7

def test_depth(bst):
    assert bst.depth() == 3

def test_contains(bst):
    assert bst.contains(4)
    assert not bst.contains(11)

def test_balance(bst):
    assert bst.balance() == 0

def test_pre_order(bst):
    assert list(bst.pre_order()) == [5, 3, 2, 4, 8, 7, 10]

def test_in_order(bst):
    assert list(bst.in_order()) == [2, 3, 4, 5, 7, 8, 10]

def test_post_order(bst):
    assert list(bst.post_order()) == [2, 4, 3, 7, 10, 8, 5]

def test_breadth_first(bst):
    assert list(bst.breadth_first()) == [5, 3, 8, 2, 4, 7, 10]

def test_delete(bst):
    bst.delete(3)
    assert not bst.contains(3)
    assert bst.size() == 6