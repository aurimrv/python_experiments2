import pytest
import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_listnode_initialization():
    node = ListNode(1, 'A')
    assert node.key == 1
    assert node.val == 'A'
    assert node.prev is None
    assert node.next is None

def test_lru_cache_initialization():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.terminal_value
    assert cache.head.val == cache.terminal_value
    assert cache.tail.key == cache.terminal_value
    assert cache.tail.val == cache.terminal_value
    assert len(cache.lookup_map) == 0

def test_put_method():
    cache = LruCache(2)
    cache.put(1, 'A')
    cache.put(2, 'B')
    
    assert cache.get(1) == 'A'
    assert cache.get(2) == 'B'

def test_get_method():
    cache = LruCache(2)
    cache.put(1, 'A')
    cache.put(2, 'B')
    
    assert cache.get(1) == 'A'
    assert cache.get(2) == 'B'
    
    cache.put(3, 'C')  # This should evict 'A'
    assert cache.get(1) == -1

def test_put_multiple_times():
    cache = LruCache(2)
    cache.put(1, 'A')
    cache.put(2, 'B')
    
    cache.put(1, 'Z')  # Update value of key 1
    assert cache.get(1) == 'Z'