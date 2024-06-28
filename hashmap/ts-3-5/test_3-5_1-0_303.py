import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

@pytest.fixture
def hashmap():
    return HashMap()

def test_insert(hashmap):
    hashmap.insert('key1', 'value1')
    assert hashmap.get('key1') == 'value1'

    hashmap.insert('key2', 'value2')
    assert hashmap.get('key2') == 'value2'

def test_get(hashmap):
    hashmap.insert('key1', 'value1')
    hashmap.insert('key2', 'value2')

    assert hashmap.get('key1') == 'value1'
    assert hashmap.get('key2') == 'value2'

def test_delete(hashmap):
    hashmap.insert('key1', 'value1')
    hashmap.insert('key2', 'value2')

    val = hashmap.delete('key1')
    assert val == ('key1', 'value1')
    with pytest.raises(KeyError):
        hashmap.get('key1')

def test_hash_functions():
    assert djb2('abc') == 193485963
    assert sdbm('abc') == 417419622498
    assert lose_lose('abc') == 294

    assert djb2('xyz') != djb2('abc')
    assert sdbm('xyz') != sdbm('abc')
    assert lose_lose('xyz') != lose_lose('abc')