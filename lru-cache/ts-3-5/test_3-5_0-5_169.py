import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

def test_list_node():
    node = ListNode(1, 'A')
    assert node.key == 1
    assert node.val == 'A'
    assert node.next is None
    assert node.prev is None

def test_lru_cache_init():
    with pytest.raises(ValueError):
        LruCache(0)
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.terminal_value
    assert cache.tail.val == cache.terminal_value

def test_lru_cache_put():
    cache = LruCache(2)
    cache.put(1, 'A')
    cache.put(2, 'B')
    assert cache.get(1) == 'A'
    cache.put(3, 'C')  # This should evict key 2
    assert cache.get(2) == -1

def test_lru_cache_get():
    cache = LruCache(2)
    cache.put(1, 'A')
    cache.put(2, 'B')
    assert cache.get(1) == 'A'
    assert cache.get(2) == 'B'
    cache.put(3, 'C')  # This should evict key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 'C'

def test_lru_cache_add_remove():
    cache = LruCache(2)
    node1 = ListNode(1, 'A')
    node2 = ListNode(2, 'B')
    cache._add(node1)
    assert cache.head.next == node1
    assert cache.tail.prev == node1
    cache._add(node2)
    assert cache.head.next == node1
    assert cache.tail.prev == node2
    cache._remove(node1)
    assert cache.head.next == node2
    assert cache.tail.prev == node2
