import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    return Bst([4, 2, 6, 1, 3, 5, 7])

def test_insert(sample_tree):
    sample_tree.insert(8)
    assert sample_tree.size() == 8
    assert sample_tree.contains(8) == True

    sample_tree.insert(1)
    assert sample_tree.size() == 8  # Size should not change if value already exists
    assert sample_tree.contains(1) == True

def test_search(sample_tree):
    assert sample_tree.search(4).val == 4
    assert sample_tree.search(10) == None

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(3) == True
    assert sample_tree.contains(9) == False

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [4, 2, 1, 3, 6, 5, 7]

def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [1, 2, 3, 4, 5, 6, 7]

def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [1, 3, 2, 5, 7, 6, 4]

def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [4, 2, 6, 1, 3, 5, 7]

def test_delete(sample_tree):
    sample_tree.delete(3)
    assert sample_tree.size() == 6
    assert sample_tree.contains(3) == False

    sample_tree.delete(4)
    assert sample_tree.size() == 5
    assert sample_tree.contains(4) == False