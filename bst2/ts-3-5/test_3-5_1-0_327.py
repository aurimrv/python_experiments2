import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst, Node

@pytest.fixture
def bst_data():
    return [5, 3, 7, 2, 4, 6, 8]

@pytest.fixture
def setup_bst(bst_data):
    bst = Bst(bst_data)
    return bst

def test_node_creation():
    node = Node(5)
    assert node.val == 5
    assert node.left == None
    assert node.right == None

def test_insert(setup_bst):
    setup_bst.insert(9)
    assert setup_bst.size() == 8
    assert setup_bst.search(9).val == 9

def test_search(setup_bst):
    assert setup_bst.search(4).val == 4
    assert setup_bst.search(10) is None

def test_depth(setup_bst):
    assert setup_bst.depth() == 3

def test_contains(setup_bst):
    assert setup_bst.contains(3) == True
    assert setup_bst.contains(10) == False

def test_balance(setup_bst):
    assert setup_bst.balance() == 0

def test_pre_order(setup_bst):
    assert list(setup_bst.pre_order()) == [5, 3, 2, 4, 7, 6, 8]

def test_in_order(setup_bst):
    assert list(setup_bst.in_order()) == [2, 3, 4, 5, 6, 7, 8]

def test_post_order(setup_bst):
    assert list(setup_bst.post_order()) == [2, 4, 3, 6, 8, 7, 5]

def test_breadth_first(setup_bst):
    assert list(setup_bst.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]