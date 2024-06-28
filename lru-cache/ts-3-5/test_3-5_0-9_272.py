import os
import sys

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

@pytest.fixture
def lru_cache():
    return LruCache(3)

def test_put(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(1) == 'a'

def test_get_existing_key(lru_cache):
    lru_cache.put(2, 'b')
    assert lru_cache.get(2) == 'b'

def test_put_capacity_exceeded(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')
    assert lru_cache.get(1) == -1

def test_get_nonexistent_key(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(2) == -1

def test_get_updates_usage_order(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.get(1)
    lru_cache.put(4, 'd')
    assert lru_cache.get(2) == -1