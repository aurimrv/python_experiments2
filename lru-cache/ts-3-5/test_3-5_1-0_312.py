import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

class TestLruCache:

    @pytest.fixture
    def cache_fixture(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        return cache

    def test_put(self, cache_fixture):
        cache = cache_fixture
        cache.put(3, 'c')
        assert cache.head.next.val == 'b'
        assert cache.tail.prev.val == 'c'
        
        cache.put(4, 'd')
        assert cache.head.next.val == 'c'
        assert cache.tail.prev.val == 'd'

    def test_get(self, cache_fixture):
        cache = cache_fixture
        assert cache.get(1) == 'a'
        assert cache.get(2) == 'b'
        
        cache.put(3, 'c')
        assert cache.get(3) == 'c'
        assert cache.get(4) == -1

    def test__add(self, cache_fixture):
        cache = cache_fixture
        node = ListNode(5, 'e')
        cache._add(node)
        assert cache.head.next.val == 'a'
        assert cache.tail.prev.val == 'e'

    def test__remove(self, cache_fixture):
        cache = cache_fixture
        node = ListNode(5, 'e')
        cache._add(node)
        cache._remove(node)
        assert cache.head.next.val == 'a'
        assert cache.tail.prev.val == 'b'   # Fixed assertion here to match the expected value