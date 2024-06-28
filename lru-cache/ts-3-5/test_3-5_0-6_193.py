import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_list_node_init():
    node = ListNode(1, 'value')
    assert node.key == 1
    assert node.val == 'value'
    assert node.next is None
    assert node.prev is None

def test_lru_cache_init():
    cache = LruCache(5)
    assert cache.capacity == 5
    assert cache.head.key == LruCache.terminal_value
    assert cache.tail.val == LruCache.terminal_value
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
    assert len(cache.lookup_map) == 0

def test_lru_cache_put():
    cache = LruCache(3)
    cache.put(1, 'one')
    assert cache.lookup_map[1].val == 'one'
    cache.put(2, 'two')
    assert cache.lookup_map[2].val == 'two'
    cache.put(3, 'three')
    assert cache.lookup_map[3].val == 'three'
    cache.put(4, 'four')
    assert 1 not in cache.lookup_map

def test_lru_cache_get():
    cache = LruCache(3)
    cache.put(1, 'one')
    cache.put(2, 'two')
    cache.put(3, 'three')
    assert cache.get(1) == 'one'
    cache.put(4, 'four')
    assert cache.get(2) == -1

def test_lru_cache_add():
    cache = LruCache(3)
    node = ListNode(1, 'one')
    cache._add(node)
    assert cache.head.next == node
    assert cache.tail.prev == node

def test_lru_cache_remove():
    cache = LruCache(3)
    node = ListNode(1, 'one')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head