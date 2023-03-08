import pytest
from naive_tree import NaiveBinaryTree
from tree_node import BinaryTreeNode

def make_simple_tree():
    tree = NaiveBinaryTree()
    tree.head = BinaryTreeNode(3, None)
    tree.head.left = BinaryTreeNode(5, tree.head)
    tree.head.right = BinaryTreeNode(7, tree.head)
    return tree
    
def make_complex_tree():
    tree = NaiveBinaryTree()
    tree.head = BinaryTreeNode(12, None)
    tree.head.left = BinaryTreeNode(3, tree.head)
    tree.head.right = BinaryTreeNode(6, tree.head)
    tree.head.left.right = BinaryTreeNode(8, tree.head.left)
    tree.head.right.right = BinaryTreeNode(2, tree.head.right)
    tree.head.left.right.right = BinaryTreeNode(17, tree.head.left.right)
    return tree

def test_pre_order_traversal():
    tree = make_simple_tree()
    assert tree.pre_order_traversal() == [3,5,7]

    tree = make_complex_tree()
    assert tree.pre_order_traversal() == [12,3,8,17,6,2]

def test_in_order_traversal():
    tree = make_simple_tree()
    assert tree.in_order_traversal() == [5,3,7]

    tree = make_complex_tree()
    assert tree.in_order_traversal() == [3,8,17,12,6,2]

def test_post_order_traversal():
    tree = make_simple_tree()
    assert tree.post_order_traversal() == [5,7,3]

    tree = make_complex_tree()
    assert tree.post_order_traversal() == [17,8,3,2,6,12]

def test_level_oreder_traversal():
    tree = make_simple_tree()
    assert tree.level_order_traversal() == [3,5,7]

    tree = make_complex_tree()
    assert tree.level_order_traversal() == [12,3,6,8,2,17]

def test_print():
    tree = make_simple_tree()
    assert tree.__str__() == '[3, 5, 7]'

