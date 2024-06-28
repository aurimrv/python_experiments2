import os
import sys
import pytest

# Add the project directory to sys.path
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
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
    assert len(cache.lookup_map) == 0

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'one')
    assert len(cache.lookup_map) == 1
    assert cache.head.next.key == 1
    assert cache.tail.prev.key == 1

    cache.put(2, 'two')
    assert len(cache.lookup_map) == 2
    assert cache.head.next.key == 1
    assert cache.tail.prev.key == 2

def test_lru_cache_get():
    cache = LruCache(2)
    cache.put(1, 'one')
    cache.put(2, 'two')

    assert cache.get(1) == 'one'
    assert cache.head.next.key == 2
    assert cache.tail.prev.key == 1

def test_lru_cache_add():
    cache = LruCache(2)
    node = ListNode(1, 'one')
    cache._add(node)
    assert cache.head.next == node
    assert cache.tail.prev == node

def test_lru_cache_remove():
    cache = LruCache(2)
    node = ListNode(1, 'one')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
    assert len(cache.lookup_map) == 0