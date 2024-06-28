import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

class TestLRUCache:

    def test_init(self):
        capacity = 5
        cache = LruCache(capacity)
        assert cache.head.key == cache.tail.val == LruCache.terminal_value
        assert cache.head.next == cache.tail
        assert cache.tail.prev == cache.head
        assert cache.lookup_map == {}
        assert cache.capacity == capacity

    def test_put_get_single(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'

    def test_put_get_multiple(self):
        cache = LruCache(3)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')
        assert cache.get(1) == 'a'
        assert cache.get(2) == 'b'
        assert cache.get(3) == 'c'

    def test_put_eviction(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')
        assert cache.get(1) == -1

    def test_get_missing_key(self):
        cache = LruCache(3)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(3) == -1

    def test_add_node(self):
        cache = LruCache(2)
        node = ListNode(1, 'a')
        cache._add(node)
        assert cache.head.next == node
        assert node.prev == cache.head
        assert cache.tail.prev == node

    def test_remove_node(self):
        cache = LruCache(2)
        node = ListNode(1, 'a')
        cache._add(node)
        cache._remove(node)
        assert cache.head.next == cache.tail
        assert cache.tail.prev == cache.head