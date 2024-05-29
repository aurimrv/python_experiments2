import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from bst2 import Bst

@pytest.fixture
def bst_fixture():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    return bst

def test_insert(bst_fixture):
    bst_fixture.insert(1)
    assert bst_fixture.size() == 8
    assert bst_fixture.root.left.left.left.val == 1

def test_search(bst_fixture):
    node = bst_fixture.search(4)
    assert node.val == 4

def test_size(bst_fixture):
    assert bst_fixture.size() == 7

def test_depth(bst_fixture):
    assert bst_fixture.depth() == 4

def test_contains(bst_fixture):
    assert bst_fixture.contains(6) == True
    assert bst_fixture.contains(9) == False

def test_balance(bst_fixture):
    assert bst_fixture.balance() == 0

def test_pre_order(bst_fixture):
    pre_order_gen = bst_fixture.pre_order()
    expected_values = [5, 3, 2, 4, 7, 6, 8]
    for val in pre_order_gen:
        assert val == expected_values.pop(0)

def test_in_order(bst_fixture):
    in_order_gen = bst_fixture.in_order()
    expected_values = [2, 3, 4, 5, 6, 7, 8]
    for val in in_order_gen:
        assert val == expected_values.pop(0)

def test_post_order(bst_fixture):
    post_order_gen = bst_fixture.post_order()
    expected_values = [2, 4, 3, 6, 8, 7, 5]
    for val in post_order_gen:
        assert val == expected_values.pop(0)

def test_breadth_first(bst_fixture):
    breadth_first_gen = bst_fixture.breadth_first()
    expected_values = [5, 3, 7, 2, 4, 6, 8]
    for val in breadth_first_gen:
        assert val == expected_values.pop(0)

def test_delete(bst_fixture):
    bst_fixture.delete(2)
    assert bst_fixture.size() == 6
    assert bst_fixture.root.left.left.val == 3