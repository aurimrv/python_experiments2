import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def lru_cache_2_capacity():
    return LruCache(2)

def test_lru_cache_init(lru_cache_2_capacity):
    assert lru_cache_2_capacity.capacity == 2
    assert lru_cache_2_capacity.head.key == lru_cache_2_capacity.tail.key
    assert lru_cache_2_capacity.head.val == lru_cache_2_capacity.tail.val

def test_put_get_single_item(lru_cache_2_capacity):
    lru_cache_2_capacity.put(1, 'one')
    assert lru_cache_2_capacity.get(1) == 'one'

def test_put_multiple_items_drop_lru(lru_cache_2_capacity):
    lru_cache_2_capacity.put(1, 'one')
    lru_cache_2_capacity.put(2, 'two')
    lru_cache_2_capacity.put(3, 'three')  # Should drop 'one'
    assert lru_cache_2_capacity.get(1) == -1
    assert lru_cache_2_capacity.get(2) == 'two'
    assert lru_cache_2_capacity.get(3) == 'three'

def test_get_nonexistent_key(lru_cache_2_capacity):
    assert lru_cache_2_capacity.get(1) == -1

def test_add_remove_methods(lru_cache_2_capacity):
    node = ListNode(1, 'one')
    lru_cache_2_capacity._add(node)
    assert lru_cache_2_capacity.head.next == node
    assert lru_cache_2_capacity.tail.prev == node

    lru_cache_2_capacity._remove(node)
    assert lru_cache_2_capacity.head.next.key != 1
    assert lru_cache_2_capacity.tail.prev.key != 1