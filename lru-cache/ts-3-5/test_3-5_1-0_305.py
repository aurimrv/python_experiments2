import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode
class TestListNode:
    def test_node_creation(self):
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.prev is None
        assert node.next is None

# Test cases for LruCache
class TestLruCache:
    def test_cache_capacity(self):
        with pytest.raises(ValueError):
            LruCache(0)

    def test_put_get_capacity(self):
        lru_cache = LruCache(3)
        lru_cache.put(1, 'a')
        lru_cache.put(2, 'b')
        lru_cache.put(3, 'c')
        assert lru_cache.get(1) == 'a'
        assert lru_cache.get(2) == 'b'
        assert lru_cache.get(3) == 'c'
    
    def test_put_capacity_exceeded(self):
        lru_cache = LruCache(2)
        lru_cache.put(1, 'a')
        lru_cache.put(2, 'b')
        lru_cache.put(3, 'c')  # Exceed capacity, should drop least recently used
        assert lru_cache.get(1) == -1
        assert lru_cache.get(2) == 'b'
        assert lru_cache.get(3) == 'c'

    def test_get_nonexistent_key(self):
        lru_cache = LruCache(2)
        lru_cache.put(1, 'a')
        assert lru_cache.get(2) == -1

    def test_put_update_existing_key(self):
        lru_cache = LruCache(2)
        lru_cache.put(1, 'a')
        lru_cache.put(2, 'b')
        lru_cache.put(1, 'updated_a')  # Update existing key
        assert lru_cache.get(1) == 'updated_a'
        assert lru_cache.get(2) == 'b'

    def test_put_remove_least_recently_used(self):
        lru_cache = LruCache(2)
        lru_cache.put(1, 'a')
        lru_cache.put(2, 'b')
        lru_cache.get(1)  # Access key 1
        lru_cache.put(3, 'c')  # Exceed capacity, should drop least recently used (key 2)
        assert lru_cache.get(1) == 'a'
        assert lru_cache.get(2) == -1
        assert lru_cache.get(3) == 'c'