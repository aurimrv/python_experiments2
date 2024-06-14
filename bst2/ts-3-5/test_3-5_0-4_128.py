import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    tree = Bst([10, 5, 15, 3, 7, 12, 17])
    return tree

def test_insert(sample_tree):
    assert sample_tree.size() == 7
    sample_tree.insert(20)
    assert sample_tree.size() == 8

def test_search(sample_tree):
    assert sample_tree.search(15).val == 15
    assert sample_tree.search(8) is None

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(5) is True
    assert sample_tree.contains(11) is False

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [10, 5, 3, 7, 15, 12, 17]

def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [3, 5, 7, 10, 12, 15, 17]

def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [3, 7, 5, 12, 17, 15, 10]

def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [10, 5, 15, 3, 7, 12, 17]

def test_delete(sample_tree):
    sample_tree.delete(7)
    assert sample_tree.size() == 6
    assert sample_tree.contains(7) is False