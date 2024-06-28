import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def cache():
    return LruCache(2)

def test_put_get(cache):
    cache.put(1, "a")
    assert cache.get(1) == "a"

def test_put_get_multiple(cache):
    cache.put(1, "a")
    cache.put(2, "b")
    assert cache.get(1) == "a"
    assert cache.get(2) == "b"

def test_put_exceed_capacity(cache):
    cache.put(1, "a")
    cache.put(2, "b")
    cache.put(3, "c")
    assert cache.get(1) == -1

def test_put_existing_key(cache):
    cache.put(1, "a")
    cache.put(1, "x")
    assert cache.get(1) == "x"

def test_remove(cache):
    cache.put(1, "a")
    cache.put(2, "b")
    cache.put(3, "c")
    assert cache.get(1) == -1

def test_get_non_existing_key(cache):
    cache.put(1, "a")
    assert cache.get(2) == -1