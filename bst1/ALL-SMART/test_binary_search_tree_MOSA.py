#Pyguin test cases converted from bst1/MOSA/seed_1706/test_binary_search_tree.py
import pytest
import binary_search_tree as module_0

def test_case_0():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'

def test_case_1():
    list_0 = []
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(list_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.in_order_traversal()
    var_2 = binary_search_tree_0.search(var_1)

def test_case_2():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.search(binary_search_tree_0)
    var_1 = binary_search_tree_0.in_order_traversal()

def test_case_3():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.in_order_traversal()

def test_case_4():
    binary_search_tree_0 = module_0.BinarySearchTree()

def test_case_5():
    list_0 = []
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(list_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.min()
    var_2 = binary_search_tree_0.insert(var_1)
    var_3 = binary_search_tree_0.insert(list_0)
    var_4 = binary_search_tree_0.delete(var_1)

def test_case_6():
    none_type_0 = None
    binary_search_tree_0 = module_0.BinarySearchTree()

def test_case_7():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.merge(binary_search_tree_0)

def test_case_8():
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

def test_case_9():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(list_1)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.insert(list_1)

def test_case_10():
    binary_search_tree_0 = module_0.BinarySearchTree()
    binary_search_tree_1 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_1.merge(binary_search_tree_1)
    var_1 = binary_search_tree_1.insert(binary_search_tree_1)
    assert f'{type(binary_search_tree_1.head).__module__}.{type(binary_search_tree_1.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_2 = binary_search_tree_1.merge(binary_search_tree_0)
    var_3 = binary_search_tree_1.min()
    var_4 = binary_search_tree_1.in_order_traversal()
    var_5 = binary_search_tree_1.search(binary_search_tree_1)
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'tree_node.BinaryTreeNode'
    assert var_5.left is None
    assert var_5.right is None
    assert f'{type(var_5.value).__module__}.{type(var_5.value).__qualname__}' == 'binary_search_tree.BinarySearchTree'
    assert var_5.parent is None

def test_case_11():
    list_0 = []
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(list_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.in_order_traversal()
    var_2 = binary_search_tree_0.insert(var_1)
    var_3 = binary_search_tree_0.insert(list_0)

def test_case_12():
    list_0 = []
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(list_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.in_order_traversal()
    var_2 = binary_search_tree_0.in_order_traversal()
    var_3 = binary_search_tree_0.insert(var_2)
    var_4 = binary_search_tree_0.insert(list_0)
    var_5 = binary_search_tree_0.insert(list_0)

def test_case_13():
    list_0 = []
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(list_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.in_order_traversal()
    var_2 = binary_search_tree_0.insert(var_1)
    var_3 = binary_search_tree_0.search(var_1)
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'tree_node.BinaryTreeNode'
    assert var_3.left is None
    assert var_3.right is None
    assert var_3.value == [[]]
    assert f'{type(var_3.parent).__module__}.{type(var_3.parent).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_4 = binary_search_tree_0.insert(list_0)
    assert f'{type(var_3.left).__module__}.{type(var_3.left).__qualname__}' == 'tree_node.BinaryTreeNode'

def test_case_14():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(list_1)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.search(list_0)
    var_2 = binary_search_tree_0.insert(list_1)
    var_3 = binary_search_tree_0.insert(list_1)
