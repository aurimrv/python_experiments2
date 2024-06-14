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

def test_insert(sample_tree):
    sample_tree.insert(6)
    assert sample_tree.size() == 8

def test_search(sample_tree):
    node = sample_tree.search(4)
    assert node.val == 4

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(8) == True

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order_traversal(sample_tree):
    traversal = list(sample_tree.pre_order())
    assert traversal == [5, 3, 2, 4, 8, 7, 9]

def test_in_order_traversal(sample_tree):
    traversal = list(sample_tree.in_order())
    assert traversal == [2, 3, 4, 5, 7, 8, 9]

def test_post_order_traversal(sample_tree):
    traversal = list(sample_tree.post_order())
    assert traversal == [2, 4, 3, 7, 9, 8, 5]

def test_breadth_first_traversal(sample_tree):
    traversal = list(sample_tree.breadth_first())
    assert traversal == [5, 3, 8, 2, 4, 7, 9]

def test_delete(sample_tree):
    sample_tree.delete(8)
    assert sample_tree.size() == 6