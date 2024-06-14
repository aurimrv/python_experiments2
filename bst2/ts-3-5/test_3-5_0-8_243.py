import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_bst():
    sample_data = [10, 5, 15, 3, 7, 12, 17]
    return Bst(sample_data)

def test_insert(sample_bst):
    sample_bst.insert(20)
    assert sample_bst.size() == 8

    assert sample_bst.search(20).val == 20

def test_search(sample_bst):
    assert sample_bst.search(10).val == 10
    assert sample_bst.search(100) is None

def test_size(sample_bst):
    assert sample_bst.size() == 7

def test_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_contains(sample_bst):
    assert sample_bst.contains(5) == True
    assert sample_bst.contains(100) == False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    assert list(sample_bst.pre_order()) == [10, 5, 3, 7, 15, 12, 17]

def test_in_order(sample_bst):
    assert list(sample_bst.in_order()) == [3, 5, 7, 10, 12, 15, 17]

def test_post_order(sample_bst):
    assert list(sample_bst.post_order()) == [3, 7, 5, 12, 17, 15, 10]

def test_breadth_first(sample_bst):
    assert list(sample_bst.breadth_first()) == [10, 5, 15, 3, 7, 12, 17]

def test_delete(sample_bst):
    sample_bst.delete(5)
    assert sample_bst.size() == 6

    assert sample_bst.search(5) is None