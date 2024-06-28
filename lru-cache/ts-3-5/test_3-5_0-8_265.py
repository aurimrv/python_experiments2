import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test for ListNode class
def test_list_node_init():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

# Test for LruCache class
def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    assert cache.get(1) == 'a'
    cache.put(2, 'b')
    assert cache.get(2) == 'b'

def test_lru_cache_put_capacity_check():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')  # Should evict 1
    assert cache.get(1) == -1

def test_lru_cache_get():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(2) == 'b'
    assert cache.get(1) == 'a'
  
def test_lru_cache_get_non_existent_key():
    cache = LruCache(3)
    cache.put(1, 'a')
    assert cache.get(2) == -1

def test_lru_cache_get_updates_order():
    cache = LruCache(3)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    cache.get(1)  # 1 should now be the most recently used
    cache.put(4, 'd')  # Should evict 2
    assert cache.get(2) == -1

def test_lru_cache_private_add():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    assert cache.head.next == node
    assert node.prev == cache.head
    assert node.next == cache.tail
    assert cache.tail.prev == node

def test_lru_cache_private_remove():
    cache = LruCache(2)
    node = ListNode(1, 'a')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
