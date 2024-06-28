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
    assert hashmap.get('key1') == 'value1'

    hashmap.insert('key2', 'value2')
    assert hashmap.get('key2') == 'value2'

def test_delete(hashmap):
    hashmap.insert('key1', 'value1')
    assert hashmap.delete('key1') == ('key1', 'value1')

    with pytest.raises(KeyError):
        hashmap.get('key1')

def test_djb2():
    assert djb2('key1') == 6385400191
    assert djb2('key2') == 6385400192

def test_sdbm():
    assert sdbm('key1') == 30205197788543922
    assert sdbm('key2') == 30205197788543923

def test_lose_lose():
    assert lose_lose('key1') == 378
    assert lose_lose('key2') == 379