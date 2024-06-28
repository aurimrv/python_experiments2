import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

# Test cases for ListNode class
class TestListNode:
    def test_node_creation(self):
        node = ListNode(1, 'value')
        assert node.key == 1
        assert node.val == 'value'

# Test cases for LruCache class
class TestLruCache:
    def test_cache_initialization(self):
        cache = LruCache(3)
        assert len(cache.lookup_map) == 0
        assert cache.capacity == 3

    def test_put_and_get_methods(self):
        cache = LruCache(2)
        cache.put(1, 'value1')
        assert cache.get(1) == 'value1'

    def test_put_capacity_exceeded(self):
        cache = LruCache(2)
        cache.put(1, 'value1')
        cache.put(2, 'value2')
        cache.put(3, 'value3')  # This should exceed capacity, evicting the least recently used
        assert cache.get(1) == -1  # 'value1' should be evicted

    def test_get_nonexistent_key(self):
        cache = LruCache(2)
        cache.put(1, 'value1')
        assert cache.get(2) == -1  # Key 2 is not in the cache

    def test_put_duplicate_key(self):
        cache = LruCache(2)
        cache.put(1, 'value1')
        cache.put(1, 'updated_value')  # Update the value for key 1
        assert cache.get(1) == 'updated_value'

    def test_put_same_key_multiple_times(self):
        cache = LruCache(2)
        cache.put(1, 'value1')
        cache.put(1, 'updated_value')
        cache.put(1, 'new_value')  # Updating key 1 multiple times
        assert cache.get(1) == 'new_value'  # The last update should reflect in the cache

    def test_get_nonexistent_key_multiple_times(self):
        cache = LruCache(2)
        cache.put(1, 'value1')
        assert cache.get(2) == -1
        assert cache.get(2) == -1  # Multiple attempts to get a non-existent key