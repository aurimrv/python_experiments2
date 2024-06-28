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
    assert node.prev is None
    assert node.next is None

def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.terminal_value
    assert cache.tail.val == cache.terminal_value
    assert len(cache.lookup_map) == 0

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'value1')
    cache.put(2, 'value2')
    assert len(cache.lookup_map) == 2

def test_lru_cache_get():
    cache = LruCache(2)
    cache.put(1, 'value1')
    cache.put(2, 'value2')
    assert cache.get(1) == 'value1'
    assert cache.get(2) == 'value2'

def test_lru_cache_add_remove():
    cache = LruCache(3)
    node1 = ListNode(1, 'value1')
    node2 = ListNode(2, 'value2')
    cache._add(node1)
    cache._add(node2)
    assert cache.head.next.key == 1
    cache._remove(node1)
    assert cache.head.next.key == 2
