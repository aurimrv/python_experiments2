import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from lru_cache import ListNode, LruCache

@pytest.fixture
def lru_cache_instance():
    return LruCache(3)

def test_lru_cache_put(lru_cache_instance):
    lru_cache_instance.put(1, 'one')
    assert lru_cache_instance.get(1) == 'one'

    lru_cache_instance.put(2, 'two')
    assert lru_cache_instance.get(2) == 'two'

def test_lru_cache_get(lru_cache_instance):
    lru_cache_instance.put(1, 'one')
    lru_cache_instance.put(2, 'two')
    
    assert lru_cache_instance.get(1) == 'one'
    assert lru_cache_instance.get(2) == 'two'

def test_lru_cache_put_overflow(lru_cache_instance):
    lru_cache_instance.put(1, 'one')
    lru_cache_instance.put(2, 'two')
    lru_cache_instance.put(3, 'three')
    
    assert lru_cache_instance.get(1) == 'one'
    assert lru_cache_instance.get(2) == 'two'
    assert lru_cache_instance.get(3) == 'three'

    lru_cache_instance.put(4, 'four')
    assert lru_cache_instance.get(1) == -1

def test_lru_cache_get_not_found(lru_cache_instance):
    lru_cache_instance.put(1, 'one')
    lru_cache_instance.put(2, 'two')
    
    assert lru_cache_instance.get(3) == -1

def test_lru_cache_add(lru_cache_instance):
    node = ListNode('test_key', 'test_value')
    lru_cache_instance._add(node)
    
    assert lru_cache_instance.get('test_key') == -1

def test_lru_cache_remove(lru_cache_instance):
    node = ListNode('test_key', 'test_value')
    lru_cache_instance._add(node)
    
    lru_cache_instance._remove(node)
    assert lru_cache_instance.get('test_key') == -1