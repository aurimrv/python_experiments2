import sys
import os
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

class TestListNode:
    # Test cases for the ListNode class
    def test_list_node_creation(self):
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.next is None
        assert node.prev is None

    def test_list_node_update(self):
        node = ListNode(2, 'b')
        node.key = 3
        node.val = 'c'
        assert node.key == 3
        assert node.val == 'c'

class TestLruCache:
    def test_lru_cache_init(self):
        cache = LruCache(3)
        assert cache.capacity == 3
        assert cache.head.key == cache.terminal_value
        assert cache.tail.key == cache.terminal_value
        assert len(cache.lookup_map) == 0

    def test_lru_cache_put(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert len(cache.lookup_map) == 2
        assert cache.head.next.key == 1
        assert cache.tail.prev.key == 2

    def test_lru_cache_get(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'
        assert cache.head.next.key == 2
        assert cache.tail.prev.key == 1

    def test_lru_cache_put_capacity_exceeded(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')
        assert len(cache.lookup_map) == 2
        assert 1 not in cache.lookup_map
        assert 2 in cache.lookup_map
        assert 3 in cache.lookup_map