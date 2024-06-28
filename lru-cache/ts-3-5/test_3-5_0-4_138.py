import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

class TestListNode:
    def test_list_node_creation(self):
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.next is None
        assert node.prev is None

class TestLruCache:
    def test_lru_cache_capacity(self):
        with pytest.raises(ValueError):
            LruCache(0)

    def test_lru_cache_put_get(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'
        cache.put(3, 'c')
        assert cache.get(2) == -1

    def test_lru_cache_put_remove(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')
        assert cache.get(1) == -1

    def test_lru_cache_put_same_key(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(1, 'b')
        assert cache.get(1) == 'b'

    def test_lru_cache_get_nonexistent_key(self):
        cache = LruCache(2)
        assert cache.get(1) == -1

    def test_lru_cache_remove_least_recently_used(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.get(1)
        cache.put(3, 'c')
        assert cache.get(2) == -1

    def test_lru_cache_add_remove_internal_functions(self):
        cache = LruCache(2)
        node1 = ListNode(1, 'a')
        node2 = ListNode(2, 'b')
        cache._add(node1)
        cache._add(node2)
        assert cache.head.next == node1
        assert cache.head.next.next == node2
        cache._remove(node1)
        assert cache.head.next == node2