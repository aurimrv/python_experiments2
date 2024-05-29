import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    data = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    return Bst(data)

def test_insert(sample_tree):
    assert sample_tree.size() == 9
    assert sample_tree.search(4).val == 4

def test_search(sample_tree):
    assert sample_tree.search(10).val == 10
    assert sample_tree.search(99) is None

def test_size(sample_tree):
    assert sample_tree.size() == 9

def test_depth(sample_tree):
    assert sample_tree.depth() == 4

def test_contains(sample_tree):
    assert sample_tree.contains(7) is True
    assert sample_tree.contains(99) is False

def test_balance(sample_tree):
    assert sample_tree.balance() == -2  # Unbalanced

def test_pre_order(sample_tree):
    expected_result = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    result = [val for val in sample_tree.pre_order()]
    assert result == expected_result

def test_in_order(sample_tree):
    expected_result = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    result = [val for val in sample_tree.in_order()]
    assert result == expected_result

def test_post_order(sample_tree):
    expected_result = [1, 4, 7, 6, 3, 13, 14, 10, 8]
    result = [val for val in sample_tree.post_order()]
    assert result == expected_result

def test_breadth_first(sample_tree):
    expected_result = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    result = [val for val in sample_tree.breadth_first()]
    assert result == expected_result