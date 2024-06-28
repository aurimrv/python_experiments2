import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def lru_cache():
    return LruCache(3)  # Set capacity to 3 for testing purposes

def test_put_and_get(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(1) == 'a'
    lru_cache.put(2, 'b')
    assert lru_cache.get(2) == 'b'

def test_put_over_capacity(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')  # Above capacity, should drop least recently used 'a'
    assert lru_cache.get(1) == -1

def test_get_non_existing_key(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(2) == -1

def test_put_existing_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(1, 'x')  # Key 1 already exists, update its value
    assert lru_cache.get(1) == 'x'

def test_put_remove_head_node(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')  # Above capacity, should drop least recently used 'a'
    assert lru_cache.get(1) == -1

def test_put_remove_tail_node(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.get(1)
    lru_cache.get(2)  # Updating usage order, head should be 3
    lru_cache.put(4, 'd')  # Above capacity, should drop least recently used 'c'
    assert lru_cache.get(3) == -1
