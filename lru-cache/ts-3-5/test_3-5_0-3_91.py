import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_list_node_init():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.tail.key == cache.terminal_value
    assert cache.head.val == cache.tail.val == cache.terminal_value
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
    assert len(cache.lookup_map) == 0

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert len(cache.lookup_map) == 2
    assert cache.head.next.key == 1
    assert cache.head.next.val == 'a'
    assert cache.head.next.next.key == 2
    assert cache.head.next.next.val == 'b'

def test_lru_cache_get():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(1) == 'a'
    assert cache.get(2) == 'b'

def test_lru_cache_put_capacity_exceeded():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert len(cache.lookup_map) == 2
    assert cache.get(1) == -1
    assert cache.get(2) == 'b'
    assert cache.get(3) == 'c'

def test_lru_cache_get_key_not_found():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(3) == -1

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