import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    tree = Bst([5, 3, 8, 2, 4, 7, 9])
    return tree

def test_node_is_leaf():
    leaf_node = Node(10)
    assert leaf_node._is_leaf() == True

def test_node_is_interior():
    interior_node = Node(10)
    interior_node.left = Node(5)
    interior_node.right = Node(15)
    assert interior_node._is_interior() == True

def test_node_onlychild():
    parent_node = Node(10)
    parent_node.left = Node(5)
    assert parent_node._onlychild() == 'left'

def test_node_side():
    parent_node = Node(10)
    child_node = Node(5, parent_node)
    parent_node.left = child_node
    assert child_node._side() == 'left'

def test_bst_insert(sample_tree):
    sample_tree.insert(6)
    assert sample_tree.size() == 8

def test_bst_search(sample_tree):
    assert sample_tree.search(4).val == 4

def test_bst_size(sample_tree):
    assert sample_tree.size() == 7

def test_bst_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_bst_contains(sample_tree):
    assert sample_tree.contains(7) == True

def test_bst_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_bst_pre_order(sample_tree):
    expected_result = [5, 3, 2, 4, 8, 7, 9]
    assert list(sample_tree.pre_order()) == expected_result

def test_bst_in_order(sample_tree):
    expected_result = [2, 3, 4, 5, 7, 8, 9]
    assert list(sample_tree.in_order()) == expected_result

def test_bst_post_order(sample_tree):
    expected_result = [2, 4, 3, 7, 9, 8, 5]
    assert list(sample_tree.post_order()) == expected_result

def test_bst_breadth_first(sample_tree):
    expected_result = [5, 3, 8, 2, 4, 7, 9]
    assert list(sample_tree.breadth_first()) == expected_result

def test_bst_delete(sample_tree):
    sample_tree.delete(4)
    assert sample_tree.size() == 6