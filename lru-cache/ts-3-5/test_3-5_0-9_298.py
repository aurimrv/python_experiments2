import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

# Test ListNode class
def test_list_node_creation():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

# Test LruCache initialization
def test_lru_cache_init():
    with pytest.raises(ValueError):
        cache = LruCache(0)  # Capacity less than 1 should raise ValueError

    cache = LruCache(3)
    assert cache.capacity == 3

# Test LruCache put method
def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')  # Adding when capacity is full should remove LRU item
    assert cache.get(1) == -1  # Key 1 should not be found after exceeding capacity
    assert cache.get(2) == 'b'  # Key 2 should still be in cache

# Test LruCache get method
def test_lru_cache_get():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    # Accessing key 1 should update its position in the cache
    assert cache.get(1) == 'a'
    cache.put(4, 'd')  # Adding new item should remove LRU item (key 2)
    assert cache.get(2) == -1  # Key 2 should not be found after exceeding capacity

# Test LruCache _add method
def test_lru_cache_add():
    cache = LruCache(2)
    node = ListNode('testkey', 'testval')
    cache._add(node)
    assert cache.head.next.key == 'testkey'  # New node should be added after head
    assert cache.tail.prev.val == 'testval'  # New node should be added before tail

# Test LruCache _remove method
def test_lru_cache_remove():
    cache = LruCache(2)
    node = ListNode('testkey', 'testval')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail  # Node should have been successfully removed from cache