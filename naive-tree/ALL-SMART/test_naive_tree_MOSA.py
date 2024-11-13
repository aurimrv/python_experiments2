#Pyguin test cases converted from naive-tree/MOSA/seed_1706/test_naive_tree.py
import pytest
import naive_tree as module_0

def test_case_0():
    naive_binary_tree_0 = module_0.NaiveBinaryTree()
    var_0 = naive_binary_tree_0.__str__()
    assert var_0 == '[]'

def test_case_1():
    naive_binary_tree_0 = module_0.NaiveBinaryTree()
    var_0 = naive_binary_tree_0.in_order_traversal()

def test_case_2():
    naive_binary_tree_0 = module_0.NaiveBinaryTree()
    var_0 = naive_binary_tree_0.post_order_traversal()

def test_case_3():
    naive_binary_tree_0 = module_0.NaiveBinaryTree()
