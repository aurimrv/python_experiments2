import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

class TestLruCache:

    def test_put_and_get_single_element(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        assert cache.get(1) == 'a'

    def test_put_capacity_reached(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # 1 should be evicted
        assert cache.get(1) == -1

    def test_put_same_key_updates_value(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(1, 'updated')
        assert cache.get(1) == 'updated'

    def test_get_nonexistent_key(self):
        cache = LruCache(2)
        assert cache.get(1) == -1

    def test_get_after_putting_multiple_elements(self):
        cache = LruCache(3)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')
        assert cache.get(1) == 'a'
        cache.put(4, 'd')  # 2 should be evicted
        assert cache.get(2) == -1

    def test_put_same_key_after_removal(self):
        cache = LruCache(2)
        cache.put(1, 'a')
        cache.put(2, 'b')
        cache.put(3, 'c')  # 1 should be evicted
        cache.put(1, 'new_a')
        assert cache.get(1) == 'new_a'

    def test_put_capacity_1(self):
        with pytest.raises(ValueError):
            cache = LruCache(0)