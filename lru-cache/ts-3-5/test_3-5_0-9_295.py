import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

# Test ListNode class

def test_list_node_creation():
    node = ListNode(1, "value")
    assert node.key == 1
    assert node.val == "value"
    assert node.prev is None
    assert node.next is None

def test_list_node_update():
    node = ListNode(1, "value")
    node.key = 2
    node.val = "new_value"
    assert node.key == 2
    assert node.val == "new_value"

# Test LruCache class

def test_lru_cache_initialization():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == LruCache.terminal_value
    assert cache.tail.key == LruCache.terminal_value
    assert len(cache.lookup_map) == 0

def test_lru_cache_put_and_get():
    cache = LruCache(3)
    cache.put(1, "value1")
    cache.put(2, "value2")
    cache.put(3, "value3")
    
    assert cache.get(1) == "value1"
    assert cache.get(2) == "value2"
    assert cache.get(3) == "value3"

def test_lru_cache_put_remove_least_recently_used():
    cache = LruCache(3)
    cache.put(1, "value1")
    cache.put(2, "value2")
    cache.put(3, "value3")
    
    cache.get(1)
    cache.put(4, "value4")
    
    assert cache.get(1) == "value1"
    assert cache.get(2) == -1
    assert cache.get(3) == "value3"
    assert cache.get(4) == "value4"

def test_lru_cache_get_nonexistent_key():
    cache = LruCache(3)
    cache.put(1, "value1")
    cache.put(2, "value2")
    
    assert cache.get(3) == -1

def test_lru_cache_capacity_validation():
    with pytest.raises(ValueError):
        LruCache(0)