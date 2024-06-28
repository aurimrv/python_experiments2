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

def test_list_node():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.next is None
    assert node.prev is None

def test_lru_cache_init(lru_cache):
    assert lru_cache.capacity == 3
    assert lru_cache.head.key == lru_cache.terminal_value
    assert lru_cache.head.val == lru_cache.terminal_value
    assert lru_cache.tail.key == lru_cache.terminal_value
    assert lru_cache.tail.val == lru_cache.terminal_value
    assert lru_cache.head.next == lru_cache.tail
    assert lru_cache.tail.prev == lru_cache.head
    assert len(lru_cache.lookup_map) == 0

def test_lru_cache_put_get(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(1) == 'a'

def test_lru_cache_put(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    assert len(lru_cache.lookup_map) == 3

def test_lru_cache_put_capacity_exceeded(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')
    assert len(lru_cache.lookup_map) == 3
    assert lru_cache.get(1) == -1

def test_lru_cache_get_key_not_found(lru_cache):
    assert lru_cache.get(1) == -1

def test_lru_cache_get_updates_order(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.get(1)
    lru_cache.put(4, 'd')
    assert lru_cache.get(2) == -1

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
