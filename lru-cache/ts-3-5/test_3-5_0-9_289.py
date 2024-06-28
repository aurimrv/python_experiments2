import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_node_initialization():
    node = ListNode(1, 'value')
    assert node.key == 1
    assert node.val == 'value'
    assert node.next is None
    assert node.prev is None

def test_lru_cache_initialization():
    capacity = 2
    lru_cache = LruCache(capacity)
    assert lru_cache.capacity == capacity
    assert lru_cache.head.key == lru_cache.terminal_value
    assert lru_cache.head.val == lru_cache.terminal_value
    assert lru_cache.tail.key == lru_cache.terminal_value
    assert lru_cache.tail.val == lru_cache.terminal_value
    assert len(lru_cache.lookup_map) == 0

def test_put_method():
    lru_cache = LruCache(2)
    lru_cache.put(1, 'value1')
    assert lru_cache.get(1) == 'value1'
    lru_cache.put(2, 'value2')
    assert lru_cache.get(2) == 'value2'
    lru_cache.put(3, 'value3')  # Exceeding capacity, should evict least recently used
    assert lru_cache.get(1) == -1

def test_get_method():
    lru_cache = LruCache(2)
    lru_cache.put(1, 'value1')
    lru_cache.put(2, 'value2')
    assert lru_cache.get(1) == 'value1'
    assert lru_cache.get(2) == 'value2'
    lru_cache.put(3, 'value3')  # Exceeding capacity, should evict least recently used
    assert lru_cache.get(1) == -1
    assert lru_cache.get(3) == 'value3'  # 'value3' should still be present

def test_add_method():
    lru_cache = LruCache(2)
    node = ListNode(1, 'value1')
    lru_cache._add(node)
    assert lru_cache.head.next == node
    assert lru_cache.tail.prev == node

def test_remove_method():
    lru_cache = LruCache(2)
    node = ListNode(1, 'value1')
    lru_cache._add(node)
    lru_cache._remove(node)
    assert lru_cache.head.next == lru_cache.tail
    assert lru_cache.tail.prev == lru_cache.head