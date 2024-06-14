import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def setup_bst():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    return bst

def test_insert(setup_bst):
    bst = setup_bst
    assert bst.size() == 7

    bst.insert(9)
    assert bst.size() == 8
    assert bst.search(9).val == 9

def test_search(setup_bst):
    bst = setup_bst
    assert bst.search(3).val == 3
    assert bst.search(10) is None

def test_size(setup_bst):
    bst = setup_bst
    assert bst.size() == 7

def test_depth(setup_bst):
    bst = setup_bst
    assert bst.depth() == 3

def test_contains(setup_bst):
    bst = setup_bst
    assert bst.contains(4) is True
    assert bst.contains(10) is False

def test_balance(setup_bst):
    bst = setup_bst
    assert bst.balance() == 0

def test_pre_order(setup_bst):
    bst = setup_bst
    expected = [5, 3, 2, 4, 7, 6, 8]
    assert list(bst.pre_order()) == expected

def test_in_order(setup_bst):
    bst = setup_bst
    expected = [2, 3, 4, 5, 6, 7, 8]
    assert list(bst.in_order()) == expected

def test_post_order(setup_bst):
    bst = setup_bst
    expected = [2, 4, 3, 6, 8, 7, 5]
    assert list(bst.post_order()) == expected

def test_breadth_first(setup_bst):
    bst = setup_bst
    expected = [5, 3, 7, 2, 4, 6, 8]
    assert list(bst.breadth_first()) == expected

def test_delete(setup_bst):
    bst = setup_bst
    bst.delete(3)
    assert bst.size() == 6
    assert bst.search(3) is None