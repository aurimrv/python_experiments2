import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

# Test cases for ListNode class
class TestListNode:
    def test_list_node_creation(self):
        node = ListNode(1, 'A')
        assert node.key == 1
        assert node.val == 'A'
        assert node.next is None
        assert node.prev is None

# Test cases for LruCache class
class TestLruCache:
    def test_lru_cache_creation(self):
        cache = LruCache(3)
        assert cache.capacity == 3
        assert cache.head.key == 0
        assert cache.tail.val == 0

    def test_put_method(self):
        cache = LruCache(2)
        cache.put(1, 'A')
        cache.put(2, 'B')
        
        assert cache.head.next.key == 1
        assert cache.head.next.val == 'A'

        cache.put(3, 'C')
        assert cache.head.next.key == 2
        assert cache.head.next.val == 'B'
        assert cache.tail.prev.key == 3
        assert cache.tail.prev.val == 'C'

    def test_get_method(self):
        cache = LruCache(2)
        cache.put(1, 'A')
        cache.put(2, 'B')

        assert cache.get(1) == 'A'
        assert cache.get(3) == -1

    def test_remove_method(self):
        cache = LruCache(2)
        cache.put(1, 'A')
        cache.put(2, 'B')

        node_to_remove = cache.head.next
        cache._remove(node_to_remove)

        assert cache.head.next.key == 2
        assert cache.head.next.val == 'B'