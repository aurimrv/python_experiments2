import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    return Bst([8, 3, 10, 1, 6, 7])

def test_insert(sample_tree):
    sample_tree.insert(5)
    assert sample_tree.contains(5) is True

def test_search(sample_tree):
    assert sample_tree.search(6).val == 6

def test_size(sample_tree):
    assert sample_tree.size() == 6

def test_depth(sample_tree):
    assert sample_tree.depth() == 4

def test_contains(sample_tree):
    assert sample_tree.contains(10) is True
    assert sample_tree.contains(2) is False

def test_balance(sample_tree):
    assert sample_tree.balance() == 2

def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [8, 3, 1, 6, 7, 10]

def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [1, 3, 6, 7, 8, 10]

def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [1, 7, 6, 3, 10, 8]

def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [8, 3, 10, 1, 6, 7]

def test_delete(sample_tree):
    sample_tree.delete(1)
    assert sample_tree.contains(1) is False