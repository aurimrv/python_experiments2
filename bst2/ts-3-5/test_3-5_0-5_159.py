import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    return Bst([5, 3, 8, 2, 4, 7, 9])

def test_node_is_leaf():
    n = Node(5)
    assert n._is_leaf() == True

def test_node_is_interior():
    n = Node(5)
    n.left = Node(3)
    n.right = Node(8)
    assert n._is_interior() == True

def test_node_onlychild():
    n = Node(5)
    n.left = Node(3)
    assert n._onlychild() == 'left'

def test_node_side():
    n1 = Node(5)
    n2 = Node(3, parent=n1)
    n1.left = n2
    assert n2._side() == 'left'

def test_bst_insert(sample_tree):
    sample_tree.insert(6)
    assert sample_tree.search(6) is not None

def test_bst_search(sample_tree):
    assert sample_tree.search(3).val == 3

def test_bst_size(sample_tree):
    assert sample_tree.size() == 7

def test_bst_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_bst_contains(sample_tree):
    assert sample_tree.contains(8) == True

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