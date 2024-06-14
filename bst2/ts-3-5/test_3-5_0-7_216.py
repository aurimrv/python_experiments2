import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    tree = Bst([8, 3, 10, 1, 6, 4, 7])
    return tree

def test_node_is_leaf():
    n = Node(5)
    assert n._is_leaf() == True

def test_node_is_interior():
    n = Node(5)
    n.left = Node(3)
    n.right = Node(7)
    assert n._is_interior() == True

def test_node_onlychild():
    n = Node(5)
    n.left = Node(3)
    assert n._onlychild() == 'left'

def test_node_side():
    parent = Node(8)
    child = Node(5, parent)
    parent.left = child
    assert child._side() == 'left'

def test_bst_insert(sample_tree):
    sample_tree.insert(5)
    assert sample_tree.size() == 8

def test_bst_search(sample_tree):
    assert sample_tree.search(6).val == 6

def test_bst_size(sample_tree):
    assert sample_tree.size() == 7

def test_bst_depth(sample_tree):
    assert sample_tree.depth() == 4

def test_bst_contains(sample_tree):
    assert sample_tree.contains(4) == True

def test_bst_balance(sample_tree):
    assert sample_tree.balance() == 2

def test_bst_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [8, 3, 1, 6, 4, 7, 10]

def test_bst_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [1, 3, 4, 6, 7, 8, 10]

def test_bst_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [1, 4, 7, 6, 3, 10, 8]

def test_bst_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [8, 3, 10, 1, 6, 4, 7]

def test_bst_delete(sample_tree):
    sample_tree.delete(6)
    assert sample_tree.size() == 6