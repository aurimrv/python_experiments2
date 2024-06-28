import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_list_node_init():
    key = "test_key"
    val = "test_value"
    node = ListNode(key, val)
    assert node.key == key
    assert node.val == val

def test_lru_cache_init():
    capacity = 3
    lru_cache = LruCache(capacity)
    assert lru_cache.capacity == capacity

def test_lru_cache_put():
    lru_cache = LruCache(3)
    lru_cache.put(1, "value1")
    assert lru_cache.get(1) == "value1"

def test_lru_cache_put_multiple():
    lru_cache = LruCache(3)
    lru_cache.put(1, "value1")
    lru_cache.put(2, "value2")
    lru_cache.put(3, "value3")
    assert lru_cache.get(1) == "value1"
    assert lru_cache.get(2) == "value2"
    assert lru_cache.get(3) == "value3"

def test_lru_cache_get():
    lru_cache = LruCache(3)
    lru_cache.put(1, "value1")
    lru_cache.put(2, "value2")
    lru_cache.put(3, "value3")
    assert lru_cache.get(1) == "value1"

def test_lru_cache_get_not_found():
    lru_cache = LruCache(3)
    lru_cache.put(1, "value1")
    assert lru_cache.get(2) == -1

def test_lru_cache_put_capacity_reached():
    lru_cache = LruCache(2)
    lru_cache.put(1, "value1")
    lru_cache.put(2, "value2")
    lru_cache.put(3, "value3")
    assert lru_cache.get(1) == -1