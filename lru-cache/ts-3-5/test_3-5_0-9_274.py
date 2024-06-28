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
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.prev is None
        assert node.next is None

    def test_node_update(self):
        node = ListNode(1, 'a')
        node.prev = ListNode(2, 'b')
        node.next = ListNode(3, 'c')
        assert node.prev.key == 2
        assert node.next.key == 3

# Test cases for LruCache class
class TestLruCache:

    def test_cache_initialization(self):
        cache = LruCache(3)
        assert cache.capacity == 3
        assert cache.head.val == cache.terminal_value

    def test_cache_put_get(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'
        cache.put(3, 'c')
        assert cache.get(2) == -1

    def test_capacity_check(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # Should remove least recently used key
        assert cache.get(1) == -1

    def test_node_add_remove(self):
        cache = LruCache(2)
        node1 = ListNode(1, 'a')
        node2 = ListNode(2, 'b')
        cache._add(node1)
        cache._add(node2)
        assert cache.head.next == node1
        cache._remove(node1)
        assert cache.head.next == node2