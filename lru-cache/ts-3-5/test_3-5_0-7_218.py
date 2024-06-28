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

def test_put_get_single_item(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(1) == 'a'

def test_put_multiple_items_get(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    assert lru_cache.get(2) == 'b'

def test_put_exceed_capacity(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')
    assert lru_cache.get(1) == -1

def test_put_existing_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(1, 'updated')
    assert lru_cache.get(1) == 'updated'

def test_get_non_existing_key(lru_cache):
    lru_cache.put(1, 'a')
    assert lru_cache.get(2) == -1

def test_put_get_multiple_items(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    assert lru_cache.get(1) == 'a'
    assert lru_cache.get(3) == 'c'

def test_put_get_single_item_when_capacity_is_one():
    with pytest.raises(ValueError):
        LruCache(0)

def test_put_get_large_number_of_items(lru_cache):
    for i in range(1000):
        lru_cache.put(i, str(i))
    assert lru_cache.get(999) == '999'
    assert lru_cache.get(0) == -1