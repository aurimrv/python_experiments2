import sys
import os
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    tree = Bst([3, 1, 5, 2, 4, 6])
    return tree

def test_insert(sample_tree):
    sample_tree.insert(7)
    assert sample_tree.size() == 7

def test_search(sample_tree):
    assert sample_tree.search(4).val == 4
    assert sample_tree.search(10) == None

def test_size(sample_tree):
    assert sample_tree.size() == 6

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(5) == True
    assert sample_tree.contains(8) == False

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [3, 1, 2, 5, 4, 6]

def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [1, 2, 3, 4, 5, 6]

def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [2, 1, 4, 6, 5, 3]

def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [3, 1, 5, 2, 4, 6]

def test_delete(sample_tree):
    sample_tree.delete(2)
    assert sample_tree.size() == 5
    assert sample_tree.search(2) == None