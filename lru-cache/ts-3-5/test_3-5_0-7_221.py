import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def lru_cache():
    return LruCache(2)

def test_list_node_initialization():
    node = ListNode(1, 'a')
    assert node.key == 1
    assert node.val == 'a'
    assert node.prev is None
    assert node.next is None

def test_lru_cache_initialization(lru_cache):
    assert lru_cache.capacity == 2
    assert lru_cache.head.key == lru_cache.terminal_value
    assert lru_cache.tail.key == lru_cache.terminal_value
    assert lru_cache.head.next == lru_cache.tail
    assert lru_cache.tail.prev == lru_cache.head
    assert lru_cache.lookup_map == {}

def test_put_method(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.lookup_map[1].val == 'a'
    lru_cache.put(2, 'b')
    assert lru_cache.lookup_map[2].val == 'b'
    lru_cache.put(3, 'c')  # Should drop key 1 as it was the least recently used
    assert 1 not in lru_cache.lookup_map

def test_get_method(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    assert lru_cache.get(1) == 'a'  # Key 1 should be the most recently used
    lru_cache.put(3, 'c')  # Should drop key 2 as it was the least recently used
    assert lru_cache.get(2) == -1  # Key 2 should not be found in the cache

def test_add_method(lru_cache):
    node = ListNode(1, 'a')
    lru_cache._add(node)
    assert lru_cache.head.next == node
    assert lru_cache.tail.prev == node

def test_remove_method(lru_cache):
    node = ListNode(1, 'a')
    lru_cache._add(node)
    lru_cache._remove(node)
    assert lru_cache.head.next == lru_cache.tail
    assert lru_cache.tail.prev == lru_cache.head