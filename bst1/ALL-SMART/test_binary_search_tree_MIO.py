#Pyguin test cases converted from bst1/MIO/seed_1706/test_binary_search_tree.py
import pytest
import binary_search_tree as module_0
import tree_node as module_1

def test_case_0():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'

def test_case_1():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'

def test_case_2():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.in_order_traversal()
    var_1 = binary_search_tree_0.insert(var_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_2 = binary_search_tree_0.insert(var_0)
    var_3 = binary_search_tree_0.insert(var_0)

def test_case_3():
    bool_0 = False
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.insert(bool_0)

def test_case_4():
    bool_0 = False
    binary_search_tree_0 = module_0.BinarySearchTree()
    bool_1 = True
    var_0 = binary_search_tree_0.insert(bool_1)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.insert(bool_0)
    var_2 = binary_search_tree_0.insert(bool_0)

def test_case_5():
    bool_0 = False
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.merge(binary_search_tree_0)
    var_1 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    float_0 = -1319.407
    var_2 = binary_search_tree_0.insert(float_0)
    var_3 = binary_search_tree_0.search(float_0)
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'tree_node.BinaryTreeNode'
    assert var_3.left is None
    assert var_3.right is None
    assert var_3.value == pytest.approx(-1319.407, abs=0.01, rel=0.01)
    assert f'{type(var_3.parent).__module__}.{type(var_3.parent).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_4 = binary_search_tree_0.search(bool_0)
    assert f'{type(var_4.left).__module__}.{type(var_4.left).__qualname__}' == 'tree_node.BinaryTreeNode'
    assert var_4.right is None
    assert var_4.value is False
    assert var_4.parent is None

def test_case_6():
    binary_search_tree_0 = module_0.BinarySearchTree()
    bool_0 = True
    var_0 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    float_0 = -924.0
    var_1 = binary_search_tree_0.search(float_0)

def test_case_7():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.search(binary_search_tree_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'tree_node.BinaryTreeNode'
    assert var_1.left is None
    assert var_1.right is None
    assert f'{type(var_1.value).__module__}.{type(var_1.value).__qualname__}' == 'binary_search_tree.BinarySearchTree'
    assert var_1.parent is None

def test_case_8():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.search(binary_search_tree_0)
    bool_0 = False
    var_1 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    float_0 = 2559.36177
    var_2 = binary_search_tree_0.search(float_0)
    var_3 = binary_search_tree_0.delete(float_0)
    binary_search_tree_1 = module_0.BinarySearchTree()

def test_case_9():
    binary_search_tree_0 = module_0.BinarySearchTree()
    bool_0 = True
    var_0 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.search(bool_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'tree_node.BinaryTreeNode'
    assert var_1.left is None
    assert var_1.right is None
    assert var_1.value is True
    assert var_1.parent is None

def test_case_10():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.search(binary_search_tree_0)

def test_case_11():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.in_order_traversal()

def test_case_12():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.in_order_traversal()

def test_case_13():
    bool_0 = True
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(bool_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    var_1 = binary_search_tree_0.merge(binary_search_tree_0)

def test_case_14():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert f'{type(binary_search_tree_0.head).__module__}.{type(binary_search_tree_0.head).__qualname__}' == 'tree_node.BinaryTreeNode'
    binary_tree_node_0 = module_1.BinaryTreeNode(binary_search_tree_0, var_0)
    binary_search_tree_1 = module_0.BinarySearchTree()
    var_1 = binary_search_tree_0.merge(binary_search_tree_1)

def test_case_15():
    binary_search_tree_0 = module_0.BinarySearchTree()
    var_0 = binary_search_tree_0.merge(binary_search_tree_0)

def test_case_16():
    binary_search_tree_0 = module_0.BinarySearchTree()

def test_case_17():
    binary_search_tree_0 = module_0.BinarySearchTree()

def test_case_18():
    binary_search_tree_0 = module_0.BinarySearchTree()
