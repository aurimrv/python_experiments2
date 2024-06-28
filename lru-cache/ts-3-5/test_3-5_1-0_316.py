import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode class

def test_list_node_initialization():
    node = ListNode(1, 'abc')
    assert node.key == 1
    assert node.val == 'abc'
    assert node.next is None
    assert node.prev is None

def test_list_node_update_key_and_value():
    node = ListNode(1, 'abc')
    node.key = 2
    node.val = 'def'
    assert node.key == 2
    assert node.val == 'def'

# Test cases for LruCache class

def test_lru_cache_initialization():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.tail.key == LruCache.terminal_value

def test_lru_cache_put_single_element():
    cache = LruCache(3)
    cache.put(1, 'a')
    assert cache.lookup_map[1].val == 'a'

def test_lru_cache_put_above_capacity():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    assert 1 not in cache.lookup_map

def test_lru_cache_get_existing_key():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(1) == 'a'

def test_lru_cache_get_non_existing_key():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(3) == -1

def test_lru_cache_put_existing_key_updates_value():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(1, 'x')
    assert cache.lookup_map[1].val == 'x'

def test_lru_cache_add_method():
    cache = LruCache(3)
    node = ListNode(1, 'a')
    cache._add(node)
    assert cache.head.next == node
    assert cache.tail.prev == node

def test_lru_cache_remove_method():
    cache = LruCache(3)
    node = ListNode(1, 'a')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head