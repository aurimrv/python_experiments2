import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

class TestListNode:
    
    def test_list_node_initialization(self):
        node = ListNode(1, 'a')
        assert node.key == 1
        assert node.val == 'a'
        assert node.next is None
        assert node.prev is None
        
    def test_list_node_linking(self):
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
        assert cache.lookup_map == {}
        assert cache.head.key == cache.tail.key == LruCache.terminal_value
        assert cache.head.next == cache.tail
        assert cache.tail.prev == cache.head
        
    def test_put_get_operations(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        
        assert cache.get(1) == 'a'
        assert cache.get(2) == 'b'
        
    def test_put_eviction(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # Forces eviction of key 1
        
        assert cache.get(1) == -1
        assert cache.get(2) == 'b'
        assert cache.get(3) == 'c'
        
    def test_get_non_existent_key(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        
        assert cache.get(3) == -1

    def test_cache_ordering(self):
        cache = LruCache(3)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')
        
        assert cache.head.next.key == 1
        assert cache.head.next.val == 'a'
        
        assert cache.get(1) == 'a'  # Move key 1 to the end
        assert cache.head.next.key == 2
        assert cache.head.next.val == 'b'

# Run tests
pytest.main()