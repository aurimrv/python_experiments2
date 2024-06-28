import sys
import os
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_list_node_init():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.prev is None
    assert node.next is None

def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == 0
    assert cache.head.val == 0
    assert cache.tail.key == 0
    assert cache.tail.val == 0

def test_lru_cache_put():
    cache = LruCache(2)
    
    cache.put(1, 'a')
    assert cache.lookup_map[1].val == 'a'
    
    cache.put(2, 'b')
    assert cache.lookup_map[2].val == 'b'

def test_lru_cache_get():
    cache = LruCache(2)
    
    cache.put(1, 'a')
    cache.put(2, 'b')
    
    assert cache.get(1) == 'a'
    assert cache.get(2) == 'b'

def test_lru_cache_put_full():
    cache = LruCache(2)
    
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')
    
    assert 1 not in cache.lookup_map
    assert cache.lookup_map[2].val == 'b'
    assert cache.lookup_map[3].val == 'c'