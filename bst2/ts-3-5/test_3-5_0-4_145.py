import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    tree = Bst([5, 3, 7, 2, 4, 6, 8])
    return tree

def test_insert(sample_tree):
    sample_tree.insert(1)
    assert sample_tree.search(1) is not None

def test_search(sample_tree):
    assert sample_tree.search(5).val == 5

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(4) is True
    assert sample_tree.contains(9) is False

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

def test_delete(sample_tree):
    sample_tree.delete(2)
    assert sample_tree.search(2) is None
    assert sample_tree.size() == 6