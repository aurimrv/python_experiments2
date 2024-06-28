import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def lru_cache():
    return LruCache(3)

def test_put(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(1) == 'a'

def test_get_nonexistent_key(lru_cache):
    assert lru_cache.get(99) == -1

def test_put_capacity_exceeded(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')  # Capacity exceeded, 'a' should be dropped
    assert lru_cache.get(1) == -1

def test_get_existing_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    assert lru_cache.get(2) == 'b'
    assert lru_cache.get(1) == 'a'

def test_get_updates_drop_order(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.get(1)  # Accessing 'a' should update drop order
    lru_cache.put(4, 'd')  # 'b' should be dropped instead of 'a'
    assert lru_cache.get(2) == -1
