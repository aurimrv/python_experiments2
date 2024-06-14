import os
import sys
import pytest

# Add the project directory to the sys path for correct import
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_bst():
    data = [50, 30, 70, 20, 40, 60, 80]
    return Bst(data)

def test_insert(sample_bst):
    sample_bst.insert(55)
    assert sample_bst.size() == 8

def test_search(sample_bst):
    node = sample_bst.search(40)
    assert node.val == 40

def test_size(sample_bst):
    assert sample_bst.size() == 7

def test_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_contains(sample_bst):
    assert sample_bst.contains(30) is True
    assert sample_bst.contains(100) is False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    pre_order_values = [50, 30, 20, 40, 70, 60, 80]
    assert list(sample_bst.pre_order()) == pre_order_values

def test_in_order(sample_bst):
    in_order_values = [20, 30, 40, 50, 60, 70, 80]
    assert list(sample_bst.in_order()) == in_order_values

def test_post_order(sample_bst):
    post_order_values = [20, 40, 30, 60, 80, 70, 50]
    assert list(sample_bst.post_order()) == post_order_values

def test_breadth_first(sample_bst):
    breadth_first_values = [50, 30, 70, 20, 40, 60, 80]
    assert list(sample_bst.breadth_first()) == breadth_first_values

def test_delete(sample_bst):
    sample_bst.delete(70)
    assert sample_bst.size() == 6
    assert sample_bst.contains(70) is False