import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

import pytest

@pytest.fixture
def lru_cache_instance():
    return LruCache(3)

def test_put(lru_cache_instance):
    lru_cache_instance.put('a', 1)
    lru_cache_instance.put('b', 2)
    
    assert lru_cache_instance.get('a') == 1
    assert lru_cache_instance.get('b') == 2

def test_get_key_not_found(lru_cache_instance):
    assert lru_cache_instance.get('c') == -1

def test_put_eviction(lru_cache_instance):
    lru_cache_instance.put('c', 3)
    lru_cache_instance.put('d', 4)
    lru_cache_instance.put('e', 5)

    assert lru_cache_instance.get('c') == 3
    assert lru_cache_instance.get('d') == 4
    assert lru_cache_instance.get('e') == 5

def test_put_eviction_max_capacity(lru_cache_instance):
    lru_cache_instance.put('f', 6)
    lru_cache_instance.put('g', 7)
    
    assert lru_cache_instance.get('a') == -1
    assert lru_cache_instance.get('b') == -1

def test_add_method(lru_cache_instance):
    node = ListNode('test', 'value')
    lru_cache_instance._add(node)
    
    assert lru_cache_instance.tail.prev.key == 'test'

def test_remove_method(lru_cache_instance):
    node = ListNode('test', 'value')
    lru_cache_instance._add(node)
    assert lru_cache_instance.tail.prev.key == 'test'
    
    lru_cache_instance._remove(node)
    
    assert lru_cache_instance.tail.prev.key != 'test'