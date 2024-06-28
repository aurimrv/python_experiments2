import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

# Test cases for ListNode class
def test_list_node_init():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_list_node_init_different_values():
    node = ListNode('key', 100)
    assert node.key == 'key'
    assert node.val == 100
    assert node.next is None
    assert node.prev is None

# Test cases for LruCache class
def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.head.key == cache.terminal_value
    assert cache.tail.val == cache.terminal_value
    assert cache.capacity == 3
    assert len(cache.lookup_map) == 0

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    assert cache.get(1) == 'a'

def test_lru_cache_put_above_capacity():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert cache.get(1) == -1

def test_lru_cache_get():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(1) == 'a'

def test_lru_cache_get_not_found():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(3) == -1

def test_lru_cache_multiple_operations():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert cache.get(1) == -1
    assert cache.get(2) == 'b'

def test_lru_cache_add_method():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    assert cache.head.next == node
    assert cache.tail.prev == node
    assert node.prev == cache.head
    assert node.next == cache.tail

def test_lru_cache_remove_method():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head