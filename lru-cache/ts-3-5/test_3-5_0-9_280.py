import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

class TestListNode:
    def test_node_initialization(self):
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.next is None
        assert node.prev is None

class TestLruCache:
    def test_cache_capacity_exception(self):
        with pytest.raises(ValueError):
            lru_cache = LruCache(0)
    
    def test_cache_put_single_element(self):
        with pytest.raises(ValueError):
            lru_cache = LruCache(1)
    
    def test_cache_put_multiple_elements(self):
        lru_cache = LruCache(2)
        lru_cache.put(1, 'a')
        lru_cache.put(2, 'b')
        assert lru_cache.get(1) == 'a'
        assert lru_cache.get(2) == 'b'
    
    def test_cache_put_eviction(self):
        lru_cache = LruCache(2)
        lru_cache.put(1, 'a')
        lru_cache.put(2, 'b')
        lru_cache.put(3, 'c')  # this should evict key 1
        assert lru_cache.get(1) == -1
        assert lru_cache.get(2) == 'b'
        assert lru_cache.get(3) == 'c'
    
    def test_cache_get_non_existing_key(self):
        lru_cache = LruCache(2)
        lru_cache.put(1, 'a')
        assert lru_cache.get(2) == -1
    
    def test_cache_get_updates_order(self):
        lru_cache = LruCache(2)
        lru_cache.put(1, 'a')
        lru_cache.put(2, 'b')
        lru_cache.get(1)  # bring 1 to the front
        lru_cache.put(3, 'c')  # this should evict key 2
        assert lru_cache.get(1) == 'a'
        assert lru_cache.get(2) == -1
        assert lru_cache.get(3) == 'c'

    def test_internal_functions_add_remove(self):
        lru_cache = LruCache(3)
        node1 = ListNode(1, 'a')
        node2 = ListNode(2, 'b')
        lru_cache._add(node1)
        assert lru_cache.head.next == node1 and lru_cache.tail.prev == node1
        lru_cache._add(node2)
        assert lru_cache.head.next == node1 and lru_cache.tail.prev == node2
        lru_cache._remove(node1)
        assert lru_cache.head.next == node2 and lru_cache.tail.prev == node2