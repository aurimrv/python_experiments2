import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode class
def test_list_node_init():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_list_node_next_prev():
    node1 = ListNode(1, 'a')
    node2 = ListNode(2, 'b')
    node1.next = node2
    node2.prev = node1

    assert node1.next == node2
    assert node2.prev == node1

# Test cases for LruCache class
def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.terminal_value
    assert cache.tail.val == cache.terminal_value
    assert len(cache.lookup_map) == 0

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')

    assert cache.get(1) == 'a'
    assert cache.get(2) == 'b'

def test_lru_cache_get():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')

    assert cache.get(1) == 'a'
    assert cache.get(2) == 'b'

def test_lru_cache_put_capacity():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')

    assert cache.get(1) == -1  # Key 1 should be evicted due to capacity
    assert cache.get(2) == 'b'
    assert cache.get(3) == 'c'

def test_lru_cache_get_not_found():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')

    assert cache.get(3) == -1  # Key 3 is not in the cache

def test_lru_cache_put_existing_key():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(1, 'x')  # Update key 1

    assert cache.get(1) == 'x'
    assert cache.get(2) == 'b'

def test_lru_cache_multiple_get():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')

    assert cache.get(1) == 'a'
    assert cache.get(2) == 'b'
    assert cache.get(3) == 'c'

    cache.get(1)  # Access key 1
    cache.get(2)  # Access key 2

    cache.put(4, 'd')  # Key 3 should be evicted

    assert cache.get(1) == 'a'
    assert cache.get(2) == 'b'
    assert cache.get(3) == -1
    assert cache.get(4) == 'd'