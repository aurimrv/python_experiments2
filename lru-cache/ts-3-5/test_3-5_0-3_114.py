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
    assert cache.head.key == 0
    assert cache.head.val == 0
    assert cache.tail.key == 0
    assert cache.tail.val == 0
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
    assert len(cache.lookup_map) == 0

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    assert cache.head.next.key == 1
    assert cache.head.next.val == 'a'
    assert cache.tail.prev.key == 1
    assert cache.tail.prev.val == 'a'
    assert len(cache.lookup_map) == 1

    cache.put(2, 'b')
    assert cache.head.next.key == 1
    assert cache.head.next.val == 'a'
    assert cache.head.next.next.key == 2
    assert cache.head.next.next.val == 'b'
    assert cache.tail.prev.key == 2
    assert cache.tail.prev.val == 'b'
    assert len(cache.lookup_map) == 2

def test_lru_cache_get():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')

    assert cache.get(1) == 'a'
    assert cache.head.next.key == 2
    assert cache.head.next.val == 'b'
    assert cache.tail.prev.key == 1
    assert cache.tail.prev.val == 'a'

    assert cache.get(3) == -1