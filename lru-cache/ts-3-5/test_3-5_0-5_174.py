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
    assert node.prev is None
    assert node.next is None

def test_list_node_init_multiple():
    node = ListNode('key', 123)
    assert node.key == 'key'
    assert node.val == 123
    assert node.prev is None
    assert node.next is None

# Test cases for LruCache class
def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.val == cache.terminal_value
    assert cache.tail.val == cache.terminal_value

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    assert cache.get(1) == 'a'

def test_lru_cache_put_capacity_reached():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')  # This should remove 'a'
    assert cache.get(1) == -1

def test_lru_cache_get():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert cache.get(2) == 'b'

def test_lru_cache_get_not_found():
    cache = LruCache(2)
    cache.put(1, 'a')
    assert cache.get(2) == -1

def test_lru_cache_get_updates_order():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    cache.get(1)
    cache.put(4, 'd')  # This should remove 'b'
    assert cache.get(2) == -1

def test_lru_cache_private_add():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    assert cache.head.next == node

def test_lru_cache_private_remove():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
