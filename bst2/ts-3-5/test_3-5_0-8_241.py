import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Node, Bst

@pytest.fixture
def sample_tree():
    tree = Bst([5, 3, 8, 2, 4, 7, 9])
    return tree

def test_node_creation():
    node = Node(5)
    assert node.val == 5
    assert node.right is None
    assert node.left is None
    assert node.parent is None
    assert node.height == 1

def test_is_leaf():
    node = Node(5)
    assert node._is_leaf() is True

def test_is_interior():
    node = Node(5)
    assert node._is_interior() is False

def test_onlychild():
    node = Node(5)
    assert node._onlychild() is None

def test_side():
    node1 = Node(5)
    node2 = Node(6, parent=node1)
    node1.right = node2
    assert node2._side() == 'right'

def test_bst_insert(sample_tree):
    sample_tree.insert(6)
    assert sample_tree.search(6).val == 6

def test_bst_search(sample_tree):
    assert sample_tree.search(4).val == 4

def test_bst_size(sample_tree):
    assert sample_tree.size() == 7

def test_bst_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_bst_contains(sample_tree):
    assert sample_tree.contains(8) is True

def test_bst_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_bst_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [5, 3, 2, 4, 8, 7, 9]

def test_bst_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [2, 3, 4, 5, 7, 8, 9]

def test_bst_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [2, 4, 3, 7, 9, 8, 5]

def test_bst_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [5, 3, 8, 2, 4, 7, 9]

def test_bst_delete(sample_tree):
    sample_tree.delete(3)
    assert sample_tree.search(3) is None