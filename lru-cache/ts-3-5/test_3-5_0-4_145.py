import os
import sys
import pytest

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
        assert node.next is None
        assert node.prev is None

# Test cases for LruCache class
class TestLruCache:
    def test_cache_initialization(self):
        cache = LruCache(3)
        assert cache.capacity == 3
        assert cache.head.key == cache.tail.key == LruCache.terminal_value
        assert cache.head.val == cache.tail.val == LruCache.terminal_value
        assert cache.head.next == cache.tail
        assert cache.tail.prev == cache.head
        assert len(cache.lookup_map) == 0

    def test_put_method(self):
        cache = LruCache(2)
        cache.put(1, "value1")
        cache.put(2, "value2")
        assert len(cache.lookup_map) == 2
        assert cache.head.next.key == 1
        assert cache.head.next.val == "value1"
        assert cache.tail.prev.key == 2
        assert cache.tail.prev.val == "value2"

    def test_get_method(self):
        cache = LruCache(2)
        cache.put(1, "value1")
        cache.put(2, "value2")
        assert cache.get(1) == "value1"
        assert cache.head.next.key == 2
        assert cache.tail.prev.key == 1

    def test_put_method_capacity_reached(self):
        cache = LruCache(2)
        cache.put(1, "value1")
        cache.put(2, "value2")
        cache.put(3, "value3")
        assert len(cache.lookup_map) == 2
        assert cache.get(1) == -1
        assert cache.get(2) == "value2"
        assert cache.get(3) == "value3"

    def test_get_method_key_not_found(self):
        cache = LruCache(2)
        cache.put(1, "value1")
        cache.put(2, "value2")
        assert cache.get(3) == -1

    def test_add_method(self):
        cache = LruCache(2)
        node = ListNode(1, "value")
        cache._add(node)
        assert cache.head.next == node
        assert cache.tail.prev == node

    def test_remove_method(self):
        cache = LruCache(2)
        node = ListNode(1, "value")
        cache._add(node)
        cache._remove(node)
        assert cache.head.next == cache.tail
        assert cache.tail.prev == cache.head