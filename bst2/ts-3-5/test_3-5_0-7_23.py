import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

@pytest.fixture
def sample_tree():
    tree = Bst([4, 2, 6, 1, 3, 5, 7])
    return tree

def test_node_is_leaf():
    node = Node(5)
    assert node._is_leaf() == True

def test_node_is_interior():
    node = Node(5)
    node.left = Node(3)
    node.right = Node(7)
    assert node._is_interior() == True

def test_node_onlychild():
    node = Node(5)
    node.left = Node(3)
    assert node._onlychild() == 'left'

def test_node_side():
    parent = Node(5)
    child = Node(3, parent)
    parent.left = child
    assert child._side() == 'left'

def test_bst_insert(sample_tree):
    sample_tree.insert(8)
    assert sample_tree.search(8) is not None

def test_bst_search(sample_tree):
    assert sample_tree.search(6).val == 6

def test_bst_size(sample_tree):
    assert sample_tree.size() == 7

def test_bst_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_bst_contains(sample_tree):
    assert sample_tree.contains(3) == True

def test_bst_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_bst_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [4, 2, 1, 3, 6, 5, 7]

def test_bst_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [1, 2, 3, 4, 5, 6, 7]

def test_bst_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [1, 3, 2, 5, 7, 6, 4]

def test_bst_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [4, 2, 6, 1, 3, 5, 7]

def test_bst_delete(sample_tree):
    sample_tree.delete(3)
    assert sample_tree.search(3) is None