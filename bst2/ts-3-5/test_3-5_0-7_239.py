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
    assert sample_tree.search(6).val == 6

def test_search(sample_tree):
    assert sample_tree.search(4).val == 4
    assert sample_tree.search(10) is None

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(2) is True
    assert sample_tree.contains(11) is False

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [5, 3, 2, 4, 8, 7, 9]

def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [2, 3, 4, 5, 7, 8, 9]

def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [2, 4, 3, 7, 9, 8, 5]

def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [5, 3, 8, 2, 4, 7, 9]

def test_delete(sample_tree):
    sample_tree.delete(4)
    assert sample_tree.contains(4) is False
    assert sample_tree.size() == 6