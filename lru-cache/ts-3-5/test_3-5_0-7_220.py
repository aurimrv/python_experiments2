import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

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
            cache = LruCache(0)

    def test_cache_put_get(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'
        assert cache.get(2) == 'b'

    def test_cache_put_max_capacity(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # this should remove the least recently used key 'a'
        assert cache.get(1) == -1
        assert cache.get(2) == 'b'
        assert cache.get(3) == 'c'

    def test_cache_get_nonexistent_key(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        assert cache.get(2) == -1

    def test_cache_put_existing_key(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(1, 'x')  # update the value for key 1
        assert cache.get(1) == 'x'

    def test_cache_put_get_multiple_times(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # this should remove key 'a'
        assert cache.get(1) == -1
        cache.put(4, 'd')  # this should remove key 'b'
        assert cache.get(2) == -1
        assert cache.get(3) == 'c'
        assert cache.get(4) == 'd'