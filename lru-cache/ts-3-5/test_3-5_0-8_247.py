import os
import sys
import pytest

# Add project directory to sys.path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

# Import the file for testing
from lru_cache import ListNode, LruCache

# Test ListNode Class
def test_list_node_init():
    node = ListNode(1, 10)
    assert node.key == 1
    assert node.val == 10
    assert node.next is None
    assert node.prev is None

# Test LruCache Class
def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.terminal_value
    assert cache.tail.key == cache.terminal_value

def test_lru_cache_put_get():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(1) == 'a'
    cache.put(3, 'c')  # Adding new element should evict the least recently used (key=2)
    assert cache.get(2) == -1  # Evicted key should return -1

def test_lru_cache_capacity_handling():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')  # Adding new element should evict the least recently used (key=1)
    assert cache.get(1) == -1  # Evicted key should return -1

def test_lru_cache_get_non_existing_key():
    cache = LruCache(2)
    assert cache.get(1) == -1

# Test internal functions of LruCache
def test_lru_cache_add():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    assert cache.head.next == node
    assert cache.tail.prev == node

def test_lru_cache_remove():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head

# To run the above tests, you can simply execute: pytest -v