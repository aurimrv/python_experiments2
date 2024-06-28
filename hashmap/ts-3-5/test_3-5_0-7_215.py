import pytest
import os
import sys

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

def test_custom_hash_functions(hashmap):
    hashmap_custom = HashMap(hash_function=djb2)
    hashmap_custom.insert('key1', 'value1')
    assert hashmap_custom.get('key1') == 'value1'

    hashmap_custom = HashMap(hash_function=sdbm)
    hashmap_custom.insert('key2', 'value2')
    assert hashmap_custom.get('key2') == 'value2'

    hashmap_custom = HashMap(hash_function=lose_lose)
    hashmap_custom.insert('key3', 'value3')
    assert hashmap_custom.get('key3') == 'value3'