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

def test_list_node_key_val():
    node = ListNode('key', 'value')
    assert node.key == 'key'
    assert node.val == 'value'

# Test cases for LruCache class
def test_lru_cache_init_capacity():
    with pytest.raises(ValueError):
        cache = LruCache(0)

def test_lru_cache_put_get():
    cache = LruCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    assert cache.get('a') == 1
    cache.put('c', 3)  # 'b' should be evicted
    assert cache.get('b') == -1

def test_lru_cache_put_same_key():
    cache = LruCache(2)
    cache.put('a', 1)
    cache.put('a', 2)
    assert cache.get('a') == 2

def test_lru_cache_put_eviction_order():
    cache = LruCache(2)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)  # 'a' should be evicted
    assert cache.get('a') == -1
    assert cache.get('b') == 2
    assert cache.get('c') == 3

def test_lru_cache_get_key_not_found():
    cache = LruCache(2)
    cache.put('a', 1)
    assert cache.get('b') == -1

def test_lru_cache_add_remove():
    cache = LruCache(2)
    node = ListNode('test', 'value')
    cache._add(node)
    assert cache.head.next == node
    cache._remove(node)
    assert cache.head.next == cache.tail
