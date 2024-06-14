import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

@pytest.fixture
def sample_tree():
    tree = Bst([10, 5, 15, 3, 7, 12, 18])
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
    parent = Node(10)
    left_child = Node(5, parent)
    parent.left = left_child
    assert left_child._side() == 'left'

def test_bst_insert(sample_tree):
    sample_tree.insert(20)
    assert sample_tree.size() == 8

def test_bst_search(sample_tree):
    assert sample_tree.search(12).val == 12

def test_bst_size(sample_tree):
    assert sample_tree.size() == 7

def test_bst_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_bst_contains(sample_tree):
    assert sample_tree.contains(15) == True
    assert sample_tree.contains(100) == False

def test_bst_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_bst_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [10, 5, 3, 7, 15, 12, 18]

def test_bst_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [3, 5, 7, 10, 12, 15, 18]

def test_bst_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [3, 7, 5, 12, 18, 15, 10]

def test_bst_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [10, 5, 15, 3, 7, 12, 18]

def test_bst_delete(sample_tree):
    sample_tree.delete(7)
    assert sample_tree.size() == 6