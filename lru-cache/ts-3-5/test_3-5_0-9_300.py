import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

# Test cases for ListNode class
class TestListNode:
    def test_list_node_creation(self):
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.prev is None
        assert node.next is None

    def test_list_node_key_value_update(self):
        node = ListNode(1, 'a')
        node.key = 2
        node.val = 'b'
        assert node.key == 2
        assert node.val == 'b'

# Test cases for LruCache class
class TestLruCache:
    def test_lru_cache_initialization(self):
        cache = LruCache(3)
        assert cache.capacity == 3
        assert cache.head.key == cache.terminal_value
        assert cache.tail.val == cache.terminal_value

    def test_lru_cache_put_method(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.head.next.key == 1
        assert cache.tail.prev.val == 'b'

    def test_lru_cache_get_method(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        assert cache.get(1) == 'a'
        assert cache.get(2) == 'b'

    def test_lru_cache_capacity_handling(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # Capacity exceeded, should drop least recently used
        assert cache.get(1) == -1  # 'a' should be dropped
        assert cache.get(2) == 'b'
        assert cache.get(3) == 'c'

    def test_lru_cache_put_duplicate_key(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(1, 'x')  # Update key 1 value
        assert cache.get(1) == 'x'
        assert cache.get(2) == 'b'

    def test_lru_cache_get_non_existent_key(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        assert cache.get(2) == -1