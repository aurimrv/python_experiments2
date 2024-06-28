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
    hashmap.insert('key3', 'value3')
    assert hashmap.get('key3') == 'value3'

    hashmap.insert('key4', 'value4')
    assert hashmap.get('key4') == 'value4'

def test_delete(hashmap):
    hashmap.insert('key5', 'value5')
    assert hashmap.get('key5') == 'value5'

    deleted_value = hashmap.delete('key5')
    assert deleted_value == ('key5', 'value5')

def test_custom_hash_functions(hashmap):
    hashmap = HashMap(buckets=4, hash_function=djb2)
    hashmap.insert('key1', 'value1')
    assert hashmap.get('key1') == 'value1'

    hashmap = HashMap(buckets=4, hash_function=sdbm)
    hashmap.insert('key2', 'value2')
    assert hashmap.get('key2') == 'value2'

    hashmap = HashMap(buckets=4, hash_function=lose_lose)
    hashmap.insert('key3', 'value3')
    assert hashmap.get('key3') == 'value3'