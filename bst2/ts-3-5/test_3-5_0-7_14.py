import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def sample_bst():
    return Bst([5, 3, 7, 2, 4, 6, 8])

def test_insert(sample_bst):
    sample_bst.insert(1)
    assert sample_bst.search(1).val == 1

    sample_bst.insert(3)
    assert sample_bst.search(3).val == 3

def test_search(sample_bst):
    assert sample_bst.search(7).val == 7
    assert sample_bst.search(4).val == 4

def test_size(sample_bst):
    assert sample_bst.size() == 7

def test_depth(sample_bst):
    assert sample_bst.depth() == 4

def test_contains(sample_bst):
    assert sample_bst.contains(6) == True
    assert sample_bst.contains(9) == False

def test_balance(sample_bst):
    assert sample_bst.balance() == 0

def test_pre_order(sample_bst):
    expected_output = [5, 3, 2, 4, 7, 6, 8]
    for val, expected_val in zip(sample_bst.pre_order(), expected_output):
        assert val == expected_val

def test_in_order(sample_bst):
    expected_output = [2, 3, 4, 5, 6, 7, 8]
    for val, expected_val in zip(sample_bst.in_order(), expected_output):
        assert val == expected_val

def test_post_order(sample_bst):
    expected_output = [2, 4, 3, 6, 8, 7, 5]
    for val, expected_val in zip(sample_bst.post_order(), expected_output):
        assert val == expected_val

def test_breadth_first(sample_bst):
    expected_output = [5, 3, 7, 2, 4, 6, 8]
    for val, expected_val in zip(sample_bst.breadth_first(), expected_output):
        assert val == expected_val