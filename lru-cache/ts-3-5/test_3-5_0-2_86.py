import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

class TestListNode:
    def test_list_node_init(self):
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.next is None
        assert node.prev is None

class TestLruCache:
    def test_lru_cache_init(self):
        cache = LruCache(3)
        assert cache.capacity == 3
        assert cache.head.key == cache.terminal_value
        assert cache.tail.val == cache.terminal_value
        assert len(cache.lookup_map) == 0

    def test_lru_cache_put_get(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'
        cache.put(3, 'c')  # This should remove key 2
        assert cache.get(2) == -1

    def test_lru_cache_put_remove(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # This should remove key 1
        assert cache.get(1) == -1

    def test_lru_cache_get_not_found(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        assert cache.get(2) == -1

    def test_lru_cache_add_remove(self):
        cache = LruCache(2)
        node = ListNode(1, 'a')
        cache._add(node)
        assert cache.head.next == node
        assert cache.tail.prev == node
        cache._remove(node)
        assert cache.head.next == cache.tail
        assert cache.tail.prev == cache.head