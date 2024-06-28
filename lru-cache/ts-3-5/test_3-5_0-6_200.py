import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

@pytest.fixture
def lru_cache():
    return LruCache(2)

def test_put(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(1) == 'a'

def test_get_existing_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    assert lru_cache.get(1) == 'a'

def test_get_non_existing_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    assert lru_cache.get(3) == -1

def test_put_over_capacity(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    assert lru_cache.get(1) == -1

def test_put_existing_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(1, 'x')
    assert lru_cache.get(1) == 'x'

def test_remove(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    assert lru_cache.get(1) == -1
    assert lru_cache.get(2) == 'b'

def test_empty_cache_get(lru_cache):
    assert lru_cache.get(1) == -1

def test_empty_cache_put(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(1) == 'a'