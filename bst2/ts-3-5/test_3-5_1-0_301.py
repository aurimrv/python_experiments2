import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

import pytest

@pytest.fixture
def sample_bst():
    bst = Bst([4, 2, 6, 1, 3, 5, 7])
    return bst

def test_insert(sample_bst):
    assert sample_bst.size() == 7
    sample_bst.insert(8)
    assert sample_bst.size() == 8
    assert sample_bst.contains(8) == True

def test_search(sample_bst):
    assert sample_bst.search(3).val == 3
    assert sample_bst.search(10) == None

def test_size(sample_bst):
    assert sample_bst.size() == 7

def test_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_contains(sample_bst):
    assert sample_bst.contains(6) == True
    assert sample_bst.contains(10) == False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    assert list(sample_bst.pre_order()) == [4, 2, 1, 3, 6, 5, 7]

def test_in_order(sample_bst):
    assert list(sample_bst.in_order()) == [1, 2, 3, 4, 5, 6, 7]

def test_post_order(sample_bst):
    assert list(sample_bst.post_order()) == [1, 3, 2, 5, 7, 6, 4]

def test_breadth_first(sample_bst):
    assert list(sample_bst.breadth_first()) == [4, 2, 6, 1, 3, 5, 7]

def test_delete(sample_bst):
    sample_bst.delete(5)
    assert sample_bst.size() == 6
    assert sample_bst.contains(5) == False