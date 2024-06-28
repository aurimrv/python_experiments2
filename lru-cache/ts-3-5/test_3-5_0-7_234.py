import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode
def test_list_node_init():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_list_node_key():
    node = ListNode('key', 'value')
    assert node.key == 'key'

# Test cases for LruCache
def test_lru_cache_init():
    cache = LruCache(5)
    assert cache.capacity == 5
    assert cache.lookup_map == {}
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head

def test_lru_cache_put_get():
    cache = LruCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    assert cache.get('a') == 1
    cache.put('c', 3)
    assert cache.get('b') == -1

def test_lru_cache_capacity():
    cache = LruCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    assert cache.get('a') == -1

def test_lru_cache_remove():
    cache = LruCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    assert 'a' not in cache.lookup_map

def test_lru_cache_get_non_existing_key():
    cache = LruCache(2)
    cache.put('a', 1)
    assert cache.get('b') == -1

# Test cases for internal methods
def test_lru_cache_add():
    cache = LruCache(2)
    node = ListNode('a', 1)
    cache._add(node)
    assert cache.head.next == node
    assert node.prev == cache.head
    assert node.next == cache.tail
    assert cache.tail.prev == node

def test_lru_cache_remove():
    cache = LruCache(2)
    node = ListNode('a', 1)
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
