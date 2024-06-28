import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

@pytest.fixture
def hashmap():
    return HashMap()

def test_insert(hashmap):
    hashmap.insert(1, 'apple')
    assert hashmap.get(1) == 'apple'
    
    hashmap.insert(2, 'banana')
    assert hashmap.get(2) == 'banana'

def test_get(hashmap):
    hashmap.insert(1, 'apple')
    hashmap.insert(2, 'banana')
    
    assert hashmap.get(1) == 'apple'
    assert hashmap.get(2) == 'banana'

def test_delete(hashmap):
    hashmap.insert(1, 'apple')
    hashmap.insert(2, 'banana')
    
    assert hashmap.delete(1) == (1, 'apple')
    with pytest.raises(KeyError):
        hashmap.get(1)

def test_djb2():
    assert djb2('test') == 6385723493

def test_sdbm():
    assert sdbm('test') == 32745785343201586

def test_lose_lose():
    assert lose_lose('test') == 448