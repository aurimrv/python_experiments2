import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_list_node_constructor():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_lru_cache_constructor():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.terminal_value
    assert cache.head.val == cache.terminal_value
    assert cache.tail.key == cache.terminal_value
    assert cache.tail.val == cache.terminal_value
    assert len(cache.lookup_map) == 0

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    assert cache.lookup_map[1].val == 'a'
    cache.put(2, 'b')
    assert cache.lookup_map[2].val == 'b'

def test_lru_cache_get():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(1) == 'a'
    assert cache.get(2) == 'b'
    assert cache.get(3) == -1

def test_lru_cache_put_capacity_exceeded():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert 1 not in cache.lookup_map
    assert cache.lookup_map[2].val == 'b'
    assert cache.lookup_map[3].val == 'c'

def test_lru_cache_get_updates_order():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.get(1)
    cache.put(3, 'c')
    assert 2 not in cache.lookup_map
    assert cache.lookup_map[1].val == 'a'
    assert cache.lookup_map[3].val == 'c'

def test_lru_cache_add_method():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    assert cache.head.next == node
    assert cache.tail.prev == node

def test_lru_cache_remove_method():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head