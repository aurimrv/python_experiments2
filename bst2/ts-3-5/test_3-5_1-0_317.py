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
    sample_tree.insert(9)
    assert sample_tree.size() == 8
    
    sample_tree.insert(3)
    assert sample_tree.size() == 8
    
def test_search(sample_tree):
    assert sample_tree.search(5).val == 5
    assert sample_tree.search(8) is None

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(6) == True
    assert sample_tree.contains(8) == False

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    traversal = list(sample_tree.pre_order())
    assert traversal == [4, 2, 1, 3, 6, 5, 7]

def test_in_order(sample_tree):
    traversal = list(sample_tree.in_order())
    assert traversal == [1, 2, 3, 4, 5, 6, 7]

def test_post_order(sample_tree):
    traversal = list(sample_tree.post_order())
    assert traversal == [1, 3, 2, 5, 7, 6, 4]

def test_breadth_first(sample_tree):
    traversal = list(sample_tree.breadth_first())
    assert traversal == [4, 2, 6, 1, 3, 5, 7]

def test_delete(sample_tree):
    sample_tree.delete(1)
    assert sample_tree.size() == 6
    assert sample_tree.contains(1) == False