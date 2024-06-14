import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def bst_tree():
    return Bst([5, 3, 7, 2, 4, 6, 8])

def test_insert(bst_tree):
    bst_tree.insert(9)
    assert bst_tree.contains(9) == True

def test_search(bst_tree):
    assert bst_tree.search(4).val == 4

def test_size(bst_tree):
    assert bst_tree.size() == 7

def test_depth(bst_tree):
    assert bst_tree.depth() == 3

def test_contains(bst_tree):
    assert bst_tree.contains(2) == True

def test_balance(bst_tree):
    assert bst_tree.balance() == 0

def test_pre_order(bst_tree):
    assert list(bst_tree.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(bst_tree):
    assert list(bst_tree.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(bst_tree):
    assert list(bst_tree.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(bst_tree):
    assert list(bst_tree.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]