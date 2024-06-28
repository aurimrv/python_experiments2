import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

class TestListNode:
    def test_node_creation(self):
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.next is None
        assert node.prev is None

class TestLruCache:
    def test_cache_capacity(self):
        with pytest.raises(ValueError):
            LruCache(0)
    
    def test_put_and_get(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'
        cache.put(3, 'c')  # 'b' should be dropped as it was the least recently used
        assert cache.get(2) == -1

    def test_put_existing_key(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(1, 'x')  # update value for key 1
        assert cache.get(1) == 'x'

    def test_get_non_existing_key(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        assert cache.get(2) == -1

    def test_remove_least_recently_used(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.get(1)  # access key 1 to make it most recently used
        cache.put(3, 'c')  # 'b' should be dropped as it was the least recently used
        assert cache.get(2) == -1

    def test_remove_least_recently_used_multiple(self):
        cache = LruCache(3)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')
        cache.get(1)  # access key 1 to make it most recently used
        cache.get(2)  # access key 2 to make it most recently used
        cache.put(4, 'd')  # 'c' should be dropped as it was the least recently used
        assert cache.get(3) == -1

    def test_get_from_empty_cache(self):
        cache = LruCache(2)
        assert cache.get(1) == -1

    def test_put_capacity_exceeded(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # capacity exceeded, 'a' should be dropped
        assert cache.get(1) == -1