import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

# Test cases for ListNode class
def test_list_node_init():
    key = 1
    val = 'A'
    node = ListNode(key, val)
    assert node.key == key
    assert node.val == val
    assert node.next is None
    assert node.prev is None

def test_list_node_init_multiple():
    key = 10
    val = 'Z'
    node = ListNode(key, val)
    assert node.key == key
    assert node.val == val
    assert node.next is None
    assert node.prev is None

# Test cases for LruCache class
def test_lru_cache_init():
    capacity = 3
    lru_cache = LruCache(capacity)
    assert lru_cache.capacity == capacity
    assert lru_cache.head.key == 0
    assert lru_cache.tail.key == 0
    assert lru_cache.head.next == lru_cache.tail
    assert lru_cache.tail.prev == lru_cache.head

def test_lru_cache_init_invalid_capacity():
    with pytest.raises(ValueError):
        LruCache(0)

def test_lru_cache_put():
    capacity = 2
    lru_cache = LruCache(capacity)
    lru_cache.put(1, 'A')
    assert lru_cache.get(1) == 'A'

def test_lru_cache_get_not_found():
    lru_cache = LruCache(3)
    assert lru_cache.get(5) == -1

def test_lru_cache_put_above_capacity():
    capacity = 2
    lru_cache = LruCache(capacity)
    lru_cache.put(1, 'A')
    lru_cache.put(2, 'B')
    lru_cache.put(3, 'C')
    assert lru_cache.get(1) == -1

def test_lru_cache_get_reorders():
    capacity = 2
    lru_cache = LruCache(capacity)
    lru_cache.put(1, 'A')
    lru_cache.put(2, 'B')
    lru_cache.get(1)
    lru_cache.put(3, 'C')
    assert lru_cache.get(2) == -1

def test_lru_cache_add():
    lru_cache = LruCache(5)
    node = ListNode(10, 'X')
    lru_cache._add(node)
    assert lru_cache.head.next == node
    assert lru_cache.tail.prev == node

def test_lru_cache_remove():
    lru_cache = LruCache(5)
    node = ListNode(10, 'X')
    lru_cache._add(node)
    lru_cache._remove(node)
    assert lru_cache.head.next == lru_cache.tail
    assert lru_cache.tail.prev == lru_cache.head