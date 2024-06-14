import os
import sys
import pytest
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def example_tree():
    return Bst([5, 2, 8, 1, 3, 7, 9])

def test_insert(example_tree):
    example_tree.insert(4)
    assert example_tree.size() == 8
    assert example_tree.contains(4)

def test_search(example_tree):
    assert example_tree.search(3).val == 3
    assert example_tree.search(6) is None

def test_size(example_tree):
    assert example_tree.size() == 7

def test_depth(example_tree):
    assert example_tree.depth() == 3

def test_contains(example_tree):
    assert example_tree.contains(7)
    assert not example_tree.contains(10)

def test_balance(example_tree):
    assert example_tree.balance() == 0

def test_pre_order(example_tree):
    assert list(example_tree.pre_order()) == [5, 2, 1, 3, 8, 7, 9]

def test_in_order(example_tree):
    assert list(example_tree.in_order()) == [1, 2, 3, 5, 7, 8, 9]

def test_post_order(example_tree):
    assert list(example_tree.post_order()) == [1, 3, 2, 7, 9, 8, 5]

def test_breadth_first(example_tree):
    assert list(example_tree.breadth_first()) == [5, 2, 8, 1, 3, 7, 9]

def test_delete(example_tree):
    example_tree.delete(7)
    assert example_tree.size() == 6
    assert not example_tree.contains(7)