import sys
import os
import pytest

# Add the project directory to the sys path
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode class
def test_list_node_init():
    node = ListNode(1, 'value')
    assert node.key == 1
    assert node.val == 'value'
    assert node.next is None
    assert node.prev is None

# Test cases for LruCache class
def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == LruCache.terminal_value
    assert cache.tail.val == LruCache.terminal_value

def test_lru_cache_put_get():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    assert cache.get(1) == 'a'
    cache.put(3, 'c')  # 'b' should be removed
    assert cache.get(2) == -1

def test_lru_cache_put_capacity_exceeded():
    cache = LruCache(2)
    cache.put(1, 'a')
    cache.put(2, 'b')
    cache.put(3, 'c')  # 'a' should be removed
    assert cache.get(1) == -1

def test_lru_cache_get_key_not_found():
    cache = LruCache(2)
    cache.put(1, 'a')
    assert cache.get(2) == -1

def test_lru_cache_add_remove():
    cache = LruCache(3)
    node1 = ListNode(1, 'a')
    node2 = ListNode(2, 'b')
    node3 = ListNode(3, 'c')
    cache._add(node1)
    cache._add(node2)
    cache._add(node3)
    assert cache.head.next == node1
    cache._remove(node2)
    assert cache.head.next == node1
    assert cache.head.next.next == node3
