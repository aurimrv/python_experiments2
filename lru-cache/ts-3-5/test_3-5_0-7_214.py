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

def test_put_get_single_element(lru_cache):
    lru_cache.put(1, 'one')
    assert lru_cache.get(1) == 'one'

def test_put_multiple_elements_get(lru_cache):
    lru_cache.put(1, 'one')
    lru_cache.put(2, 'two')
    lru_cache.put(3, 'three')
    assert lru_cache.get(1) == 'one'
    assert lru_cache.get(2) == 'two'
    assert lru_cache.get(3) == 'three'

def test_put_above_capacity_get(lru_cache):
    lru_cache.put(1, 'one')
    lru_cache.put(2, 'two')
    lru_cache.put(3, 'three')
    lru_cache.put(4, 'four')  # This should trigger removal of 'one'
    assert lru_cache.get(1) == -1
    assert lru_cache.get(2) == 'two'
    assert lru_cache.get(3) == 'three'
    assert lru_cache.get(4) == 'four'

def test_get_non_existing_key(lru_cache):
    lru_cache.put(1, 'one')
    assert lru_cache.get(2) == -1

def test_put_existing_key_get(lru_cache):
    lru_cache.put(1, 'one')
    lru_cache.put(1, 'new_one')
    assert lru_cache.get(1) == 'new_one'

def test_put_get_order(lru_cache):
    lru_cache.put(1, 'one')
    lru_cache.put(2, 'two')
    lru_cache.put(3, 'three')
    lru_cache.get(1)  # Make 'one' most recently used
    lru_cache.put(4, 'four')  # This should trigger removal of 'two'
    assert lru_cache.get(1) == 'one'
    assert lru_cache.get(2) == -1
    assert lru_cache.get(3) == 'three'
    assert lru_cache.get(4) == 'four'