import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst

@pytest.fixture
def sample_bst():
    bst = Bst([50, 30, 70, 20, 40, 60, 80])
    return bst

def test_insert_and_size(sample_bst):
    assert sample_bst.size() == 7
    sample_bst.insert(90)
    assert sample_bst.size() == 8

def test_search(sample_bst):
    assert sample_bst.search(40).val == 40
    assert sample_bst.search(100) is None

def test_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_contains(sample_bst):
    assert sample_bst.contains(20) is True
    assert sample_bst.contains(45) is False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    assert list(sample_bst.pre_order()) == [50, 30, 20, 40, 70, 60, 80]

def test_in_order(sample_bst):
    assert list(sample_bst.in_order()) == [20, 30, 40, 50, 60, 70, 80]

def test_post_order(sample_bst):
    assert list(sample_bst.post_order()) == [20, 40, 30, 60, 80, 70, 50]

def test_breadth_first(sample_bst):
    assert list(sample_bst.breadth_first()) == [50, 30, 70, 20, 40, 60, 80]

def test_delete(sample_bst):
    assert sample_bst.size() == 7
    sample_bst.delete(40)
    assert sample_bst.size() == 6
    assert sample_bst.search(40) is None