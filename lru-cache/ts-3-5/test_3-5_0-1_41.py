import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def lru_cache():
    return LruCache(2)

def test_put_get(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(1) == 'a'

def test_put_capacity(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')  # This should remove the least recently used item 'a'
    assert lru_cache.get(1) == -1

def test_get_nonexistent_key(lru_cache):
    assert lru_cache.get(99) == -1

def test_put_existing_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(1, 'x')  # Update the value for key 1
    assert lru_cache.get(1) == 'x'

def test_put_multiple_keys(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    assert lru_cache.get(1) == 'a'
    assert lru_cache.get(2) == 'b'

def test_put_capacity_with_same_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(1, 'x')  # Update the value for key 1
    lru_cache.put(2, 'b')
    assert lru_cache.get(1) == 'x'
    assert lru_cache.get(2) == 'b'