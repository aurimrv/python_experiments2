import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    data = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    return Bst(data)

def test_insert(sample_tree):
    assert sample_tree.size() == 15
    assert sample_tree.search(9).val == 9

def test_search(sample_tree):
    assert sample_tree.search(9).val == 9
    assert sample_tree.search(16) is None

def test_size(sample_tree):
    assert sample_tree.size() == 15

def test_depth(sample_tree):
    assert sample_tree.depth() == 4

def test_contains(sample_tree):
    assert sample_tree.contains(9) == True
    assert sample_tree.contains(16) == False

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]

def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 14, 12, 8]

def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

def test_delete(sample_tree):
    sample_tree.delete(9)
    assert sample_tree.contains(9) == False
    assert sample_tree.size() == 14