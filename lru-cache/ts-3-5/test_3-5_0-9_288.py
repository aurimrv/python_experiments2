import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_list_node():
    node1 = ListNode(1, 'a')
    assert node1.key == 1
    assert node1.val == 'a'
    assert node1.next is None
    assert node1.prev is None

    node2 = ListNode(2, 'b')
    assert node2.key == 2
    assert node2.val == 'b'
    assert node2.next is None
    assert node2.prev is None

def test_lru_cache_init():
    cache = LruCache(5)
    assert cache.capacity == 5
    assert cache.head.key == cache.tail.key == LruCache.terminal_value
    assert cache.head.val == cache.tail.val == LruCache.terminal_value
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')

    assert cache.lookup_map[1].val == 'a'
    assert cache.lookup_map[2].val == 'b'

    cache.put(3, 'c')
    assert len(cache.lookup_map) == 2
    assert 1 not in cache.lookup_map

def test_lru_cache_get():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')

    assert cache.get(2) == 'b'
    assert cache.get(1) == 'a'

    cache.put(4, 'd')
    assert cache.get(2) == 'b'
    assert cache.get(1) == 'a'
    assert cache.get(3) == -1

def test_lru_cache_add_remove():
    cache = LruCache(3)
    node1 = ListNode(1, 'a')
    node2 = ListNode(2, 'b')
    node3 = ListNode(3, 'c')

    cache._add(node1)
    cache._add(node2)
    cache._add(node3)

    assert cache.head.next == node1
    assert cache.tail.prev == node3

    cache._remove(node2)
    assert cache.head.next == node1
    assert cache.tail.prev == node3

    cache._remove(node3)
    assert cache.head.next == node1
    assert cache.tail.prev == node1