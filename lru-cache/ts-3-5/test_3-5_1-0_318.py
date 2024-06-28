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

    def test_list_node_update(self):
        node = ListNode(2, 'b')
        node.key = 3
        node.val = 'c'
        assert node.key == 3
        assert node.val == 'c'

class TestLruCache:

    def test_lru_cache_capacity(self):
        with pytest.raises(ValueError):
            cache = LruCache(0)

    def test_lru_cache_put_get(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'
        assert cache.get(2) == 'b'

    def test_lru_cache_get_non_existing_key(self):
        cache = LruCache(3)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(3) == -1

    def test_lru_cache_put_updates_existing_key(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'
        cache.put(1, 'c')
        assert cache.get(1) == 'c'

    def test_lru_cache_put_capacity_exceeded(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # this should remove the least recently used (LRU) item
        assert cache.get(1) == -1

    def test_lru_cache_remove_method(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        removed_node = cache.head.next
        cache._remove(removed_node)
        assert removed_node.key == 1
        assert removed_node.val == 'a'
        assert cache.head.next == cache.tail  # head -> tail

    def test_lru_cache_add_method(self):
        cache = LruCache(2)
        node = ListNode(1, 'a')
        cache._add(node)
        assert cache.head.next == node
        assert cache.tail.prev == node
        assert node.prev == cache.head
        assert node.next == cache.tail
