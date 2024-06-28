import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_list_node_creation():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_lru_cache_creation():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == LruCache.terminal_value
    assert cache.tail.val == LruCache.terminal_value
    assert len(cache.lookup_map) == 0

def test_put_method():
    cache = LruCache(2)
    cache.put(1, 'a')
    assert cache.lookup_map[1].val == 'a'
    cache.put(2, 'b')
    assert cache.lookup_map[2].val == 'b'
    cache.put(3, 'c')  # This should remove 'a' as it exceeds capacity
    assert 1 not in cache.lookup_map

def test_get_method():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(1) == 'a'
    cache.put(3, 'c')  # This should remove 'b' as it exceeds capacity
    assert cache.get(2) == -1

def test_add_method():
    cache = LruCache(2)
    node1 = ListNode(1, 'a')
    cache._add(node1)
    assert cache.head.next == node1
    assert cache.tail.prev == node1

def test_remove_method():
    cache = LruCache(2)
    node1 = ListNode(1, 'a')
    node2 = ListNode(2, 'b')
    cache._add(node1)
    cache._add(node2)
    cache._remove(node1)
    assert cache.head.next == node2
    assert cache.tail.prev == node2