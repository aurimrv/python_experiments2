import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from binary_search_tree import BinarySearchTree

def test_insert():
    tree = BinarySearchTree()
    tree.insert(5)
    assert tree.head.value == 5
    
    tree.insert(3)
    assert tree.head.left.value == 3
    
    tree.insert(7)
    assert tree.head.right.value == 7

def test_min():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    assert tree.min() == 3

def test_delete():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.delete(3)
    assert tree.head.left is None

def test_search():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    assert tree.search(3).value == 3
    assert tree.search(10) is None

def test_in_order_traversal():
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    assert tree.in_order_traversal() == [3, 5, 7]

def test_merge():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()
    tree1.insert(5)
    tree1.insert(3)
    tree2.insert(7)
    tree2.insert(9)
    tree1.merge(tree2)
    assert tree1.head.value == 12
    assert tree1.head.right.value == 9