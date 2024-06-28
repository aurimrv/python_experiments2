import os
import sys
import pytest

# Add project directory to sys path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode class
def test_list_node_initialization():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

# Test cases for LruCache class
def test_lru_cache_initialization():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.tail.key == LruCache.terminal_value
    assert cache.head.val == cache.tail.val == LruCache.terminal_value
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
    assert len(cache.lookup_map) == 0

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(1) == 'a'
    cache.put(3, 'c')
    assert cache.get(2) == -1
    assert cache.get(3) == 'c'

def test_lru_cache_get():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(1) == 'a'
    assert cache.get(2) == 'b'
    cache.put(3, 'c')
    assert cache.get(1) == -1
    assert cache.get(3) == 'c'

def test_lru_cache_edge_cases():
    with pytest.raises(ValueError):
        LruCache(0)
    with pytest.raises(ValueError):
        LruCache(-1)