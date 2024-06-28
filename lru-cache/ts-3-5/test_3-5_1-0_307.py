import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

@pytest.fixture
def empty_cache():
    capacity = 3
    lru_cache = LruCache(capacity)
    return lru_cache

def test_put_and_get_single_item(empty_cache):
    empty_cache.put(1, 'a')
    assert empty_cache.get(1) == 'a'

def test_put_multiple_items_get_last(empty_cache):
    empty_cache.put(1, 'a')
    empty_cache.put(2, 'b')
    empty_cache.put(3, 'c')
    assert empty_cache.get(3) == 'c'

def test_put_full_cache_remove_lru(empty_cache):
    empty_cache.put(1, 'a')
    empty_cache.put(2, 'b')
    empty_cache.put(3, 'c')
    empty_cache.put(4, 'd')
    assert empty_cache.get(1) == -1

def test_put_duplicate_key_updates_value(empty_cache):
    empty_cache.put(1, 'a')
    empty_cache.put(1, 'updated')
    assert empty_cache.get(1) == 'updated'

def test_put_key_above_capacity_removes_lru(empty_cache):
    empty_cache.put(1, 'a')
    empty_cache.put(2, 'b')
    empty_cache.put(3, 'c')
    empty_cache.put(4, 'd')
    empty_cache.put(5, 'e')  # Should remove 1
    assert empty_cache.get(1) == -1

def test_get_nonexistent_key_returns_minus_one(empty_cache):
    empty_cache.put(1, 'a')
    assert empty_cache.get(2) == -1