import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_tree():
    return Bst([50, 30, 20, 40, 70, 60, 80])

def test_insert(sample_tree):
    assert sample_tree.size() == 7
    sample_tree.insert(90)
    assert sample_tree.size() == 8
    assert sample_tree.search(90).val == 90

def test_search(sample_tree):
    assert sample_tree.search(40).val == 40
    assert sample_tree.search(100) is None

def test_size(sample_tree):
    assert sample_tree.size() == 7

def test_depth(sample_tree):
    assert sample_tree.depth() == 3

def test_contains(sample_tree):
    assert sample_tree.contains(60) is True
    assert sample_tree.contains(25) is False

def test_balance(sample_tree):
    assert sample_tree.balance() == 0

def test_pre_order(sample_tree):
    assert list(sample_tree.pre_order()) == [50, 30, 20, 40, 70, 60, 80]

def test_in_order(sample_tree):
    assert list(sample_tree.in_order()) == [20, 30, 40, 50, 60, 70, 80]

def test_post_order(sample_tree):
    assert list(sample_tree.post_order()) == [20, 40, 30, 60, 80, 70, 50]

def test_breadth_first(sample_tree):
    assert list(sample_tree.breadth_first()) == [50, 30, 70, 20, 40, 60, 80]

def test_delete(sample_tree):
    sample_tree.delete(20)
    assert sample_tree.size() == 6
    assert sample_tree.search(20) is None