import os
import sys
import pytest

# Add project directory to import module correctly
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_bst():
    data = [50, 30, 20, 40, 70, 60, 80]
    return Bst(data)

def test_insert(sample_bst):
    assert sample_bst.size() == 7
    sample_bst.insert(90)
    assert sample_bst.size() == 8
    assert sample_bst.contains(90) == True

def test_search(sample_bst):
    node = sample_bst.search(30)
    assert node.val == 30
    node = sample_bst.search(100)
    assert node is None

def test_size(sample_bst):
    assert sample_bst.size() == 7

def test_depth(sample_bst):
    assert sample_bst.depth() == 3

def test_contains(sample_bst):
    assert sample_bst.contains(70) == True
    assert sample_bst.contains(10) == False

def test_balance(sample_bst):
    assert sample_bst.balance() == -1

def test_pre_order(sample_bst):
    result = list(sample_bst.pre_order())
    assert result == [50, 30, 20, 40, 70, 60, 80]

def test_in_order(sample_bst):
    result = list(sample_bst.in_order())
    assert result == [20, 30, 40, 50, 60, 70, 80]

def test_post_order(sample_bst):
    result = list(sample_bst.post_order())
    assert result == [20, 40, 30, 60, 80, 70, 50]

def test_breadth_first(sample_bst):
    result = list(sample_bst.breadth_first())
    assert result == [50, 30, 70, 20, 40, 60, 80]

def test_delete(sample_bst):
    sample_bst.delete(20)
    assert sample_bst.size() == 6
    assert sample_bst.contains(20) == False