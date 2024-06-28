import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_list_node_creation():
    node = ListNode(1, 'one')
    assert node.key == 1
    assert node.val == 'one'
    assert node.next is None
    assert node.prev is None

def test_lru_cache_initialization():
    cache = LruCache(2)
    assert cache.head.val == 0
    assert cache.tail.val == 0
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
    assert cache.lookup_map == {}
    assert cache.capacity == 2

def test_put_method():
    cache = LruCache(2)
    cache.put(1, 'one')
    assert cache.lookup_map[1].val == 'one'

def test_put_method_capacity_check():
    cache = LruCache(2)
    cache.put(1, 'one')
    cache.put(2, 'two')
    cache.put(3, 'three')  # this should trigger the capacity check
    assert 1 not in cache.lookup_map  # least recently used node should be removed

def test_get_method_existing_key():
    cache = LruCache(2)
    cache.put(1, 'one')
    cache.put(2, 'two')
    assert cache.get(1) == 'one'  # accessing 1 should bring it to the front

def test_get_method_non_existing_key():
    cache = LruCache(2)
    cache.put(1, 'one')
    assert cache.get(2) == -1  # key 2 does not exist

def test_add_method():
    cache = LruCache(2)
    node = ListNode(1, 'one')
    cache._add(node)
    assert cache.head.next == node
    assert cache.tail.prev == node
    assert node.prev == cache.head
    assert node.next == cache.tail

def test_remove_method():
    cache = LruCache(2)
    node = ListNode(1, 'one')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head