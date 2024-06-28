import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

class TestLruCache:

    def test_put_method(self):
        cache = LruCache(2)
        
        cache.put(1, 1)
        assert cache.get(1) == 1
        
        cache.put(2, 2)
        assert cache.get(2) == 2

        cache.put(3, 3)  # This will trigger the removal of the least recently used item
        assert cache.get(1) == -1

    def test_get_method(self):
        cache = LruCache(2)
        
        cache.put(1, 1)
        cache.put(2, 2)
        
        assert cache.get(1) == 1
        
        cache.put(3, 3)  # This will trigger the removal of the least recently used item
        assert cache.get(2) == -1

    def test_add_method(self):
        cache = LruCache(2)

        node1 = ListNode(1, 1)
        node2 = ListNode(2, 2)

        cache._add(node1)
        cache._add(node2)

        assert cache.head.next.key == 1
        assert cache.head.next.next.key == 2

    def test_remove_method(self):
        cache = LruCache(2)

        node1 = ListNode(1, 1)
        node2 = ListNode(2, 2)

        cache._add(node1)
        cache._add(node2)
        cache._remove(node1)

        assert cache.head.next.key == 2
