import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode class
def test_list_node_initialization():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_list_node_key_value_update():
    node = ListNode(1, 'a')
    node.key = 2
    node.val = 'b'
    assert node.key == 2
    assert node.val == 'b'

# Test cases for LruCache class
def test_lru_cache_initialization():
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

def test_lru_cache_get():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert cache.get(1) == 'a'
    assert cache.get(2) == 'b'
    assert cache.get(4) == -1

def test_lru_cache_put_capacity_exceeded():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert cache.get(1) == -1

def test_lru_cache_put_existing_key():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(1, 'x')
    assert cache.get(1) == 'x'

def test_lru_cache_remove():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert cache.get(1) == -1

def test_lru_cache_get_nonexistent_key():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(3) == -1