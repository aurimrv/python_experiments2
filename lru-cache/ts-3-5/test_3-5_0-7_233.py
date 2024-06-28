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

def test_put_get(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    assert lru_cache.get(1) == 'a'
    assert lru_cache.get(2) == 'b'

def test_put_remove(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')  # Adding more items than capacity should remove the least recently used
    assert lru_cache.get(1) == -1  # 'a' should have been removed

def test_put_update(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(2, 'x')  # Updating an existing key should update the value
    assert lru_cache.get(2) == 'x'

def test_get_nonexistent_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    assert lru_cache.get(3) == -1  # Getting a key that doesn't exist should return -1

def test_capacity_check(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')
    assert len(lru_cache.lookup_map) == 3  # Capacity should be maintained