import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# ListNode class tests
def test_list_node_init():
    node = ListNode(1, 'one')
    assert node.key == 1
    assert node.val == 'one'

def test_list_node_next():
    node1 = ListNode(1, 'one')
    node2 = ListNode(2, 'two')
    
    assert node1.next is None
    assert node2.next is None

def test_list_node_prev():
    node1 = ListNode(1, 'one')
    node2 = ListNode(2, 'two')
    
    assert node1.prev is None
    assert node2.prev is None

# LruCache class tests
def test_lru_cache_init():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.terminal_value
    assert cache.tail.val == cache.terminal_value

def test_lru_cache_put():
    cache = LruCache(2)
    
    cache.put(1, 'one')
    assert cache.get(1) == 'one'
    
    cache.put(2, 'two')
    assert cache.get(2) == 'two'

def test_lru_cache_put_capacity():
    cache = LruCache(2)
    
    cache.put(1, 'one')
    cache.put(2, 'two')
    
    cache.put(3, 'three')  # Adding one more than capacity to trigger drop
    assert cache.get(1) == -1  # First element should be dropped

def test_lru_cache_get():
    cache = LruCache(2)
    
    cache.put(1, 'one')
    cache.put(2, 'two')
    
    assert cache.get(1) == 'one'
    assert cache.get(2) == 'two'
    assert cache.get(3) == -1  # Non-existing key should return -1

def test_lru_cache__add():
    cache = LruCache(2)
    
    node1 = ListNode(1, 'one')
    node2 = ListNode(2, 'two')
    
    cache._add(node1)
    assert cache.head.next == node1
    assert cache.tail.prev == node1
    
    cache._add(node2)
    assert cache.tail.prev == node2

def test_lru_cache__remove():
    cache = LruCache(2)
    
    node1 = ListNode(1, 'one')
    node2 = ListNode(2, 'two')
    
    cache._add(node1)
    cache._add(node2)
    
    cache._remove(node1)
    assert cache.head.next == node2
    assert cache.tail.prev == node2
