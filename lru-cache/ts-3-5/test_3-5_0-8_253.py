import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def create_cache():
    return LruCache(2)

def test_put_existing_key(create_cache):
    cache = create_cache
    cache.put(1, 'A')
    cache.put(2, 'B')
    cache.put(1, 'C')
    assert cache.get(1) == 'C'

def test_put_new_key(create_cache):
    cache = create_cache
    cache.put(1, 'A')
    cache.put(2, 'B')
    cache.put(3, 'C')
    assert cache.get(3) == 'C'

def test_put_capacity_exceeded(create_cache):
    cache = create_cache
    cache.put(1, 'A')
    cache.put(2, 'B')
    cache.put(3, 'C')
    assert cache.get(1) == -1

def test_get_existing_key(create_cache):
    cache = create_cache
    cache.put(1, 'A')
    cache.put(2, 'B')
    assert cache.get(2) == 'B'

def test_get_non_existing_key(create_cache):
    cache = create_cache
    cache.put(1, 'A')
    cache.put(2, 'B')
    assert cache.get(3) == -1

def test_get_refresh_key_order(create_cache):
    cache = create_cache
    cache.put(1, 'A')
    cache.put(2, 'B')
    cache.get(1)
    cache.put(3, 'C')
    assert cache.get(2) == -1

def test_add_node(create_cache):
    cache = create_cache
    node = ListNode(1, 'A')
    cache._add(node)
    assert cache.head.next.key == 1

def test_remove_node(create_cache):
    cache = create_cache
    node = ListNode(1, 'A')
    cache._add(node)
    cache._remove(node)
    assert cache.head.next == cache.tail