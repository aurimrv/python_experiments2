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

def test_put_get(lru_cache):
    lru_cache.put(1, 'value1')
    assert lru_cache.get(1) == 'value1'

def test_put_get_multiple(lru_cache):
    lru_cache.put(1, 'value1')
    lru_cache.put(2, 'value2')
    lru_cache.put(3, 'value3')
    assert lru_cache.get(1) == 'value1'
    assert lru_cache.get(2) == 'value2'
    assert lru_cache.get(3) == 'value3'

def test_put_overflow(lru_cache):
    lru_cache.put(1, 'value1')
    lru_cache.put(2, 'value2')
    lru_cache.put(3, 'value3')
    lru_cache.put(4, 'value4')
    assert lru_cache.get(1) == -1

def test_put_update_existing_key(lru_cache):
    lru_cache.put(1, 'value1')
    lru_cache.put(1, 'new_value1')
    assert lru_cache.get(1) == 'new_value1'

def test_put_same_key_increases_capacity(lru_cache):
    lru_cache.put(1, 'value1')
    lru_cache.put(1, 'new_value1')
    lru_cache.put(2, 'value2')
    assert lru_cache.get(1) == 'new_value1'

def test_get_non_existing_key(lru_cache):
    assert lru_cache.get(100) == -1