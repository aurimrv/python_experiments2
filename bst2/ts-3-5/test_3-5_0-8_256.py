import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

@pytest.fixture
def bst():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    return bst

def test_insert(bst):
    bst.insert(1)
    assert bst.size() == 8
    assert bst.depth() == 4
    
def test_search(bst):
    assert bst.search(4).val == 4
    assert bst.search(10) is None

def test_size(bst):
    assert bst.size() == 7
    bst.insert(10)
    assert bst.size() == 8

def test_depth(bst):
    assert bst.depth() == 3
    bst.insert(1)
    assert bst.depth() == 4

def test_contains(bst):
    assert bst.contains(6)
    assert not bst.contains(9)

def test_balance(bst):
    assert bst.balance() == 0

def test_pre_order(bst):
    expected = [5, 3, 2, 4, 7, 6, 8]
    assert list(bst.pre_order()) == expected

def test_in_order(bst):
    expected = [2, 3, 4, 5, 6, 7, 8]
    assert list(bst.in_order()) == expected

def test_post_order(bst):
    expected = [2, 4, 3, 6, 8, 7, 5]
    assert list(bst.post_order()) == expected

def test_breadth_first(bst):
    expected = [5, 3, 7, 2, 4, 6, 8]
    assert list(bst.breadth_first()) == expected