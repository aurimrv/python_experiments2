import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def lru_cache():
    return LruCache(3)

def test_list_node_init():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.terminal_value
    assert cache.tail.val == cache.terminal_value
    assert len(cache.lookup_map) == 0

def test_lru_cache_put(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.lookup_map[1].val == 'a'
    lru_cache.put(2, 'b')
    assert lru_cache.lookup_map[2].val == 'b'

def test_lru_cache_put_capacity_reached(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')
    assert 1 not in lru_cache.lookup_map

def test_lru_cache_get(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    assert lru_cache.get(1) == 'a'

def test_lru_cache_get_not_found(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    assert lru_cache.get(3) == -1

def test_lru_cache_add(lru_cache):
    node = ListNode(1, 'a')
    lru_cache._add(node)
    assert lru_cache.head.next == node
    assert lru_cache.tail.prev == node

def test_lru_cache_remove(lru_cache):
    node = ListNode(1, 'a')
    lru_cache._add(node)
    lru_cache._remove(node)
    assert lru_cache.head.next == lru_cache.tail
    assert lru_cache.tail.prev == lru_cache.head