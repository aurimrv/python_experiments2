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

def test_list_node_initialization():
    node = ListNode(1, "value")
    assert node.key == 1
    assert node.val == "value"
    assert node.next is None
    assert node.prev is None

def test_lru_cache_initialization():
    cache = LruCache(3)
    assert cache.capacity == 3
    assert cache.head.key == cache.tail.key == cache.terminal_value
    assert cache.head.val == cache.tail.val == cache.terminal_value
    assert cache.head.next == cache.tail
    assert cache.tail.prev == cache.head
    assert len(cache.lookup_map) == 0

def test_put_method(lru_cache):
    lru_cache.put(1, "value1")
    lru_cache.put(2, "value2")
    lru_cache.put(3, "value3")

    assert lru_cache.lookup_map == {1: lru_cache.head.next, 2: lru_cache.head.next.next, 3: lru_cache.head.next.next.next}

def test_get_method(lru_cache):
    lru_cache.put(1, "value1")
    lru_cache.put(2, "value2")
    lru_cache.put(3, "value3")

    assert lru_cache.get(2) == "value2"
    assert lru_cache.get(1) == "value1"
    assert lru_cache.get(4) == -1

def test_capacity_handling(lru_cache):
    lru_cache.put(1, "value1")
    lru_cache.put(2, "value2")
    lru_cache.put(3, "value3")
    lru_cache.put(4, "value4")

    assert len(lru_cache.lookup_map) == 3
    assert 1 not in lru_cache.lookup_map
    assert lru_cache.get(1) == -1