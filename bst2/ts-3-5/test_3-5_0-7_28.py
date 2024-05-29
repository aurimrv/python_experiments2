import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def bst():
    return Bst()

def test_insert(bst):
    bst.insert(5)
    assert bst.size() == 1
    bst.insert(2)
    assert bst.size() == 2

def test_search(bst):
    bst.insert(5)
    bst.insert(3)
    assert bst.search(3).val == 3
    assert bst.search(5).val == 5

def test_size(bst):
    assert bst.size() == 0
    bst.insert(7)
    assert bst.size() == 1
    bst.insert(4)
    assert bst.size() == 2

def test_depth(bst):
    assert bst.depth() == 0
    bst.insert(10)
    assert bst.depth() == 1
    bst.insert(5)
    assert bst.depth() == 2

def test_contains(bst):
    bst.insert(8)
    bst.insert(3)
    assert bst.contains(8) == True
    assert bst.contains(5) == False

def test_balance(bst):
    bst.insert(10)
    assert bst.balance() == 0
    bst.insert(5)
    assert bst.balance() == 1

def test_pre_order(bst):
    bst.insert(3)
    bst.insert(1)
    bst.insert(5)
    assert list(bst.pre_order()) == [3, 1, 5]

def test_in_order(bst):
    bst.insert(3)
    bst.insert(1)
    bst.insert(5)
    assert list(bst.in_order()) == [1, 3, 5]

def test_post_order(bst):
    bst.insert(3)
    bst.insert(1)
    bst.insert(5)
    assert list(bst.post_order()) == [1, 5, 3]

def test_breadth_first(bst):
    bst.insert(3)
    bst.insert(1)
    bst.insert(5)
    assert list(bst.breadth_first()) == [3, 1, 5]

def test_delete(bst):
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.delete(3)
    assert bst.size() == 2
    assert list(bst.in_order()) == [5, 7]