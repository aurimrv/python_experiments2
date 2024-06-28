import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode class
def test_list_node_init():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_list_node_update():
    node = ListNode(2, 'b')
    node.key = 3
    node.val = 'c'
    assert node.key == 3
    assert node.val == 'c'

# Test cases for LruCache class
def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.terminal_value
    assert cache.tail.val == cache.terminal_value

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

def test_lru_cache_put_capacity_exceeded():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert 1 not in cache.lookup_map
    assert cache.get(2) == 'b'
    assert cache.get(3) == 'c'

def test_lru_cache_get_key_not_found():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(3) == -1

def test_lru_cache_private_methods():
    cache = LruCache(2)
    node1 = ListNode(1, 'a')
    node2 = ListNode(2, 'b')
    cache._add(node1)
    cache._add(node2)
    assert cache.head.next == node1
    assert cache.tail.prev == node2
    cache._remove(node1)
    assert cache.head.next == node2
    assert cache.tail.prev == node2