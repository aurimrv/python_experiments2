import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

class TestListNode:
    
    def test_node_creation(self):
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.next is None
        assert node.prev is None
    
    def test_node_linkage(self):
        node1 = ListNode(1, 'a')
        node2 = ListNode(2, 'b')
        
        node1.next = node2
        node2.prev = node1
        
        assert node1.next == node2
        assert node2.prev == node1

class TestLruCache:

    def test_cache_initialization(self):
        cache = LruCache(3)
        assert cache.capacity == 3
        assert cache.head.key == cache.terminal_value
        assert cache.tail.val == cache.terminal_value
        assert len(cache.lookup_map) == 0

    def test_cache_put_get(self):
        cache = LruCache(3)
        cache.put('a', 1)
        cache.put('b', 2)
        
        assert cache.get('a') == 1
        assert cache.get('b') == 2

    def test_cache_full_capacity(self):
        cache = LruCache(2)
        cache.put('a', 1)
        cache.put('b', 2)
        cache.put('c', 3)  # Should remove 'a' as it is the least recently used
        
        assert cache.get('a') == -1
        assert cache.get('b') == 2
        assert cache.get('c') == 3

    def test_cache_lru_update(self):
        cache = LruCache(2)
        cache.put('a', 1)
        cache.put('b', 2)
        
        assert cache.get('a') == 1
        
        cache.put('c', 3)  # 'b' should be the least recently used now
        
        assert cache.get('b') == -1
        assert cache.get('a') == 1
        assert cache.get('c') == 3

    def test_cache_duplicate_put(self):
        cache = LruCache(2)
        cache.put('a', 1)
        cache.put('b', 2)
        
        assert cache.get('a') == 1
        
        cache.put('a', 10)  # Updating the value for key 'a'
        
        assert cache.get('a') == 10
        assert cache.get('b') == 2
