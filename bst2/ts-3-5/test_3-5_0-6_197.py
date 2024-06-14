import os
import sys
import pytest

# Add project directory to sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_bst():
    data = [10, 5, 15, 3, 8, 12, 18]
    return Bst(data)

def test_insert(sample_bst):
    assert sample_bst.size() == 7
    sample_bst.insert(20)
    assert sample_bst.size() == 8
    assert sample_bst.search(20).val == 20

def test_search(sample_bst):
    assert sample_bst.search(5).val == 5
    assert sample_bst.search(100) is None

def test_size(sample_bst):
    assert sample_bst.size() == 7
    sample_bst.insert(25)
    assert sample_bst.size() == 8

def test_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_contains(sample_bst):
    assert sample_bst.contains(15) is True
    assert sample_bst.contains(30) is False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    expected = [10, 5, 3, 8, 15, 12, 18]
    assert list(sample_bst.pre_order()) == expected

def test_in_order(sample_bst):
    expected = [3, 5, 8, 10, 12, 15, 18]
    assert list(sample_bst.in_order()) == expected

def test_post_order(sample_bst):
    expected = [3, 8, 5, 12, 18, 15, 10]
    assert list(sample_bst.post_order()) == expected

def test_breadth_first(sample_bst):
    expected = [10, 5, 15, 3, 8, 12, 18]
    assert list(sample_bst.breadth_first()) == expected

def test_delete(sample_bst):
    sample_bst.delete(5)
    assert sample_bst.size() == 6
    assert sample_bst.contains(5) is False
    sample_bst.delete(15)
    assert sample_bst.size() == 5
    assert sample_bst.contains(15) is False