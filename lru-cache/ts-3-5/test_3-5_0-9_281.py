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
    lru_cache.put(3, 'c')
    assert lru_cache.get(2) == 'b'
    lru_cache.put(4, 'd')
    assert lru_cache.get(3) == 'c'
    assert lru_cache.get(4) == 'd'
    assert lru_cache.get(5) == -1


def test_put_capacity(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(3, 'c')
    lru_cache.put(4, 'd')
    assert lru_cache.get(1) == -1
    assert lru_cache.get(2) == 'b'
    assert lru_cache.get(3) == 'c'
    assert lru_cache.get(4) == 'd'


def test_put_duplicate_key(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(2, 'b')
    lru_cache.put(1, 'x')
    assert lru_cache.get(1) == 'x'
    assert lru_cache.get(2) == 'b'


def test_put_same_key_multiple_times(lru_cache):
    lru_cache.put(1, 'a')
    lru_cache.put(1, 'b')
    lru_cache.put(1, 'c')
    assert lru_cache.get(1) == 'c'