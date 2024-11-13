#Pyguin test cases converted from bst1/DYNAMOSA/seed_1706/test_binary_search_tree.py
import pytest
import binary_search_tree as module_0
import tree_node as module_1

def test_case_0():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'

def test_case_1():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.search(binary_search_tree_0)
    var_1 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_2 = binary_search_tree_0.in_order_traversal()
    var_3 = binary_search_tree_0.min()

def test_case_2():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.search(binary_search_tree_0)
    var_1 = binary_search_tree_0.in_order_traversal()

def test_case_3():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.search(binary_search_tree_0)
    var_1 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'

def test_case_4():
    binary_search_tree_0 = module_0.BinarySearchTree()

def test_case_5():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.search(binary_search_tree_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'tree_node.BinaryTreeNode'
    assert var_1.left is None
    assert var_1.right is None
    assert f'{type(var_1.value).__module__}.{type(var_1.value).__qualname__}' == 'binary_search_tree.BinarySearchTree'
    assert var_1.parent is None
    var_2 = binary_search_tree_0.min()
    binary_tree_node_0 = module_1.BinaryTreeNode(var_0, var_1)
    binary_search_tree_1 = module_0.BinarySearchTree()
    var_3 = binary_search_tree_1.merge(binary_search_tree_1)

def test_case_6():
    none_type_0 = None
    binary_search_tree_0 = module_0.BinarySearchTree()

def test_case_7():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.merge(binary_search_tree_0)

def test_case_8():
    binary_search_tree_0 = module_0.BinarySearchTree()
    binary_search_tree_1 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.merge(binary_search_tree_0)
    var_1 = binary_search_tree_0.search(binary_search_tree_0)
    var_2 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_3 = binary_search_tree_0.in_order_traversal()
    binary_search_tree_2 = module_0.BinarySearchTree()
    var_4 = binary_search_tree_0.merge(binary_search_tree_2)

def test_case_9():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.in_order_traversal()
    binary_search_tree_1 = module_0.BinarySearchTree()
    bool_0 = True
    var_1 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_2 = binary_search_tree_0.insert(bool_0)

def test_case_10():
    binary_search_tree_0 = module_0.BinarySearchTree()
    bool_0 = True
    binary_search_tree_1 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_1.search(binary_search_tree_1)
    bool_1 = False
    var_2 = binary_search_tree_0.insert(bool_1)
    var_3 = binary_search_tree_0.insert(bool_1)

def test_case_11():
    binary_search_tree_0 = module_0.BinarySearchTree()
    bool_0 = True
    binary_search_tree_1 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_1.search(binary_search_tree_1)
    bool_1 = True
    var_2 = binary_search_tree_0.insert(bool_1)
    var_3 = binary_search_tree_0.insert(bool_1)

def test_case_12():
    binary_search_tree_0 = module_0.BinarySearchTree()
    bool_0 = True
    binary_search_tree_1 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_1.search(binary_search_tree_1)
    bool_1 = False
    var_1 = binary_search_tree_0.insert(bool_1)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_2 = binary_search_tree_0.insert(bool_1)
    var_3 = binary_search_tree_0.search(bool_0)
    binary_tree_node_0 = module_1.BinaryTreeNode(binary_search_tree_0, bool_0)

def test_case_13():
    bool_0 = True
    binary_search_tree_0 = module_0.BinarySearchTree()
    int_0 = -3107
    list_0 = [int_0, int_0, int_0]
    var_0 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    bool_1 = False
    var_1 = binary_search_tree_0.search(bool_1)
    float_0 = 4239.7
    binary_tree_node_0 = module_1.BinaryTreeNode(list_0, float_0)
    var_2 = binary_tree_node_0.min()
