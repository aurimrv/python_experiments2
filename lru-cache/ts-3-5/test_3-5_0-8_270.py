import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def lru_cache_instance():
    return LruCache(2)

def test_put(lru_cache_instance):
    lru_cache_instance.put(1, 'a')
    lru_cache_instance.put(2, 'b')
    assert lru_cache_instance.get(1) == 'a'
    assert lru_cache_instance.get(2) == 'b'

def test_get(lru_cache_instance):
    lru_cache_instance.put(1, 'a')
    lru_cache_instance.put(2, 'b')
    assert lru_cache_instance.get(1) == 'a'
    lru_cache_instance.put(3, 'c')
    assert lru_cache_instance.get(2) == -1

def test_put_same_key(lru_cache_instance):
    lru_cache_instance.put(1, 'a')
    lru_cache_instance.put(2, 'b')
    lru_cache_instance.put(1, 'x')
    assert lru_cache_instance.get(1) == 'x'

def test_get_not_found(lru_cache_instance):
    assert lru_cache_instance.get(1) == -1

def test_capacity_exceeded(lru_cache_instance):
    lru_cache_instance.put(1, 'a')
    lru_cache_instance.put(2, 'b')
    lru_cache_instance.put(3, 'c')
    assert lru_cache_instance.get(1) == -1