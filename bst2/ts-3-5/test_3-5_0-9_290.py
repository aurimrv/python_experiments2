import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    return Bst([5, 3, 7, 2, 4, 6, 8])

def test_insert(sample_tree):
    sample_tree.insert(1)
    assert sample_tree.size() == 8
    assert sample_tree.search(1).val == 1

def test_search(sample_tree):
    assert sample_tree.search(4).val == 4
    assert sample_tree.search(10) is None

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(6) is True
    assert sample_tree.contains(9) is False

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    expected_pre_order = [5, 3, 2, 4, 7, 6, 8]
    assert list(sample_tree.pre_order()) == expected_pre_order

def test_in_order(sample_tree):
    expected_in_order = [2, 3, 4, 5, 6, 7, 8]
    assert list(sample_tree.in_order()) == expected_in_order

def test_post_order(sample_tree):
    expected_post_order = [2, 4, 3, 6, 8, 7, 5]
    assert list(sample_tree.post_order()) == expected_post_order

def test_breadth_first(sample_tree):
    expected_breadth_first = [5, 3, 7, 2, 4, 6, 8]
    assert list(sample_tree.breadth_first()) == expected_breadth_first