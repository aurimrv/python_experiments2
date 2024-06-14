import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def prepare_bst():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    return bst

def test_insert(prepare_bst):
    assert prepare_bst.size() == 7
    prepare_bst.insert(9)
    assert prepare_bst.size() == 8

def test_search(prepare_bst):
    assert prepare_bst.search(3).val == 3
    assert prepare_bst.search(10) is None

def test_size(prepare_bst):
    assert prepare_bst.size() == 7

def test_depth(prepare_bst):
    assert prepare_bst.depth() == 3

def test_contains(prepare_bst):
    assert prepare_bst.contains(7) == True
    assert prepare_bst.contains(10) == False

def test_balance(prepare_bst):
    assert prepare_bst.balance() == 0

def test_pre_order(prepare_bst):
    assert list(prepare_bst.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(prepare_bst):
    assert list(prepare_bst.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(prepare_bst):
    assert list(prepare_bst.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(prepare_bst):
    assert list(prepare_bst.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

def test_delete(prepare_bst):
    prepare_bst.delete(3)
    assert prepare_bst.size() == 6
    assert prepare_bst.search(3) is None