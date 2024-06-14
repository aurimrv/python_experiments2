import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

import pytest

@pytest.fixture
def sample_tree():
    data = [50, 30, 70, 20, 40, 60, 80]
    return Bst(data)

def test_insert(sample_tree):
    sample_tree.insert(90)
    assert sample_tree.search(90) is not None

def test_search(sample_tree):
    assert sample_tree.search(30).val == 30

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(70) == True

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    expected_result = [50, 30, 20, 40, 70, 60, 80]
    result = [node_value for node_value in sample_tree.pre_order()]
    assert result == expected_result

def test_in_order(sample_tree):
    expected_result = [20, 30, 40, 50, 60, 70, 80]
    result = [node_value for node_value in sample_tree.in_order()]
    assert result == expected_result

def test_post_order(sample_tree):
    expected_result = [20, 40, 30, 60, 80, 70, 50]
    result = [node_value for node_value in sample_tree.post_order()]
    assert result == expected_result

def test_breadth_first(sample_tree):
    expected_result = [50, 30, 70, 20, 40, 60, 80]
    result = [node_value for node_value in sample_tree.breadth_first()]
    assert result == expected_result

def test_delete(sample_tree):
    sample_tree.delete(20)
    assert sample_tree.search(20) is None