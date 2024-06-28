import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

class TestListNode:
    def test_list_node_creation(self):
        node = ListNode(1, "value")
        assert node.key == 1
        assert node.val == "value"
        assert node.prev is None
        assert node.next is None

class TestLruCache:
    def test_lru_cache_capacity_validation(self):
        with pytest.raises(ValueError):
            cache = LruCache(0)
        
    def test_lru_cache_put_get(self):
        cache = LruCache(2)
        cache.put(1, 'one')
        cache.put(2, 'two')
        assert cache.get(1) == 'one'
        cache.put(3, 'three')  # 'two' should be removed
        assert cache.get(2) == -1

    def test_lru_cache_put_same_key(self):
        cache = LruCache(2)
        cache.put(1, 'one')
        cache.put(1, 'new_one')
        assert cache.get(1) == 'new_one'

    def test_lru_cache_put_eviction_order(self):
        cache = LruCache(3)
        cache.put(1, 'one')
        cache.put(2, 'two')
        cache.put(3, 'three')
        assert cache.get(1) == 'one'
        cache.put(4, 'four')  # 'two' should be removed
        cache.put(5, 'five')  # 'one' should be removed
        assert cache.get(2) == -1

    def test_lru_cache_get_non_existing_key(self):
        cache = LruCache(2)
        cache.put(1, 'one')
        assert cache.get(2) == -1

    def test_lru_cache_remove_method(self):
        cache = LruCache(2)
        cache.put(1, 'one')
        node = cache.lookup_map[1]
        cache._remove(node)
        assert cache.head.next == cache.tail
        assert cache.tail.prev == cache.head

    def test_lru_cache_add_method(self):
        cache = LruCache(2)
        node = ListNode(1, 'one')
        cache._add(node)
        assert cache.head.next == node
        assert cache.tail.prev == node
        assert node.prev == cache.head
        assert node.next == cache.tail