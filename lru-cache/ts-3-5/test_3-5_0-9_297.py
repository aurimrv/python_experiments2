import pytest
import os
import sys
import importlib

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

lru_cache = importlib.import_module("lru_cache")

def test_list_node_constructor():
    key = 1
    val = "value"
    node = lru_cache.ListNode(key, val)
    assert node.key == key
    assert node.val == val
    assert node.next is None
    assert node.prev is None

def test_lru_cache_constructor_capacity():
    with pytest.raises(ValueError):
        lru_cache.LruCache(0)

def test_lru_cache_put():
    cache = lru_cache.LruCache(2)
    cache.put(1, 'one')
    assert cache.get(1) == 'one'
    cache.put(2, 'two')
    assert cache.get(2) == 'two'
    cache.put(3, 'three')  # evicts key 1
    assert cache.get(1) == -1

def test_lru_cache_get():
    cache = lru_cache.LruCache(2)
    cache.put(1, 'one')
    assert cache.get(1) == 'one'
    cache.put(2, 'two')
    assert cache.get(2) == 'two'
    assert cache.get(3) == -1

def test_lru_cache_add():
    cache = lru_cache.LruCache(2)
    cache._add(lru_cache.ListNode(1, 'one'))
    assert cache.tail.prev.key == 1
    assert cache.tail.next == None

def test_lru_cache_remove():
    cache = lru_cache.LruCache(2)
    node = lru_cache.ListNode(1, 'one')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head