import os
import sys
import pytest

# Importing the module to be tested
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode class
class TestListNode:
    def test_node_creation(self):
        node = ListNode(1, "value")
        assert node.key == 1
        assert node.val == "value"
    
    def test_node_linking(self):
        node1 = ListNode(1, "value1")
        node2 = ListNode(2, "value2")
        node1.next = node2
        node2.prev = node1
        assert node1.next == node2
        assert node2.prev == node1

# Test cases for LruCache class
class TestLruCache:
    def test_cache_initialization(self):
        cache = LruCache(5)
        assert cache.capacity == 5

    def test_put_method(self):
        cache = LruCache(2)
        cache.put(1, "value1")
        cache.put(2, "value2")

        assert cache.get(1) == "value1"
        assert cache.get(2) == "value2"

        cache.put(3, "value3") 
        assert cache.get(1) == -1  # Key 1 should have been dropped

    def test_get_method(self):
        cache = LruCache(3)
        cache.put(1, "value1")
        cache.put(2, "value2")
        cache.put(3, "value3")
        
        assert cache.get(2) == "value2"
        cache.put(4, "value4")
        assert cache.get(1) == -1  # Key 1 should have been dropped

        cache.put(5, "value5")
        assert cache.get(3) == -1  # Key 3 should have been dropped

    def test_add_method(self):
        cache = LruCache(2)
        node = ListNode(1, "value1")
        cache._add(node)
        assert cache.head.next == node
        assert cache.tail.prev == node
    
    def test_remove_method(self):
        cache = LruCache(2)
        node = ListNode(1, "value1")
        cache._add(node)
        cache._remove(node)
        assert cache.head.next == cache.tail
        assert cache.tail.prev == cache.head
