import pytest
from binary_search_tree import BinarySearchTree
from tree_node import BinaryTreeNode

def make_simple_tree():
    tree = BinarySearchTree()

    tree.insert(12)
    tree.insert(7)
    tree.insert(3)
    tree.insert(18)
    tree.insert(32)
    tree.insert(1)
    tree.insert(5)

    return tree

def test_pre_order_traversal():
    tree = make_simple_tree()
    assert tree.in_order_traversal() == [1,3,5,7,12,18,32]

def test_min():
    tree = make_simple_tree()
    assert tree.min() == 1

def test_delete():
    tree = make_simple_tree()

    tree.delete(1) # delete node that has no children

    assert tree.in_order_traversal() == [3,5,7,12,18,32]

    tree.delete(18) # delete node that has 1 child, right

    assert tree.in_order_traversal() == [3,5,7,12,32]

    tree.insert(15)

    tree.delete(32) # delete node that has 1 child, left

    assert tree.in_order_traversal() == [3,5,7,12,15]

    tree.insert(8)

    tree.delete(7) # delete node that has 2 children

    assert tree.in_order_traversal() == [3,5,8,12,15]

    # miss on the delete
    tree.delete(9)

def test_search():
    tree = make_simple_tree()

    assert tree.search(12).value == 12

    assert tree.search(87) == None

    assert tree.search(3).value == 3

def test_merge():
    tree = make_simple_tree()

    tree2 = BinarySearchTree()

    tree2.insert(5)
    tree2.insert(9)
    tree2.insert(10)

    tree.merge(tree2)

    assert tree.head.value == 17
    assert tree.search(27).value == 27
    assert tree.search(42).value == 42

