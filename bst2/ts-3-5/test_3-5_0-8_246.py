import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

import bst2

@pytest.fixture
def example_tree():
    return bst2.Bst([10, 5, 15, 3, 7, 12, 20])

def test_insert(example_tree):
    example_tree.insert(25)
    assert example_tree.contains(25)
    assert example_tree.size() == 8

def test_search(example_tree):
    assert example_tree.search(15).val == 15
    assert example_tree.search(100) is None

def test_size(example_tree):
    assert example_tree.size() == 7

def test_depth(example_tree):
    assert example_tree.depth() == 3

def test_contains(example_tree):
    assert example_tree.contains(5) is True
    assert example_tree.contains(100) is False

def test_balance(example_tree):
    assert example_tree.balance() == 0

def test_pre_order(example_tree):
    assert list(example_tree.pre_order()) == [10, 5, 3, 7, 15, 12, 20]

def test_in_order(example_tree):
    assert list(example_tree.in_order()) == [3, 5, 7, 10, 12, 15, 20]

def test_post_order(example_tree):
    assert list(example_tree.post_order()) == [3, 7, 5, 12, 20, 15, 10]

def test_breadth_first(example_tree):
    assert list(example_tree.breadth_first()) == [10, 5, 15, 3, 7, 12, 20]

def test_delete(example_tree):
    example_tree.delete(12)
    assert example_tree.contains(12) is False
    assert example_tree.size() == 6