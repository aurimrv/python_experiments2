import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def empty_cache():
    return LruCache(2)

def test_put_get_value(empty_cache):
    empty_cache.put(1, 'a')
    assert empty_cache.get(1) == 'a'

def test_put_same_key_twice(empty_cache):
    empty_cache.put(1, 'a')
    empty_cache.put(1, 'b')
    assert empty_cache.get(1) == 'b'

def test_put_capacity_reached(empty_cache):
    empty_cache.put(1, 'a')
    empty_cache.put(2, 'b')
    empty_cache.put(3, 'c')
    assert empty_cache.get(1) == -1

def test_get_non_existent_key(empty_cache):
    empty_cache.put(1, 'a')
    assert empty_cache.get(2) == -1

def test_remove_least_recently_used(empty_cache):
    empty_cache.put(1, 'a')
    empty_cache.put(2, 'b')
    empty_cache.get(1)
    empty_cache.put(3, 'c')
    assert empty_cache.get(2) == -1