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


def test_insert_and_get(hashmap):
    hashmap.insert('test_key', 'test_value')
    assert hashmap.get('test_key') == 'test_value'


def test_override_insert(hashmap):
    hashmap.insert('test_key', 'initial_value')
    hashmap.insert('test_key', 'new_value')
    assert hashmap.get('test_key') == 'new_value'


def test_get_nonexistent_key_raises_key_error(hashmap):
    with pytest.raises(KeyError):
        hashmap.get('nonexistent_key')


def test_delete_key(hashmap):
    hashmap.insert('test_key', 'test_value')
    deleted_value = hashmap.delete('test_key')
    assert deleted_value == ('test_key', 'test_value')
    with pytest.raises(KeyError):
        hashmap.get('test_key')


def test_delete_nonexistent_key_raises_key_error(hashmap):
    with pytest.raises(KeyError):
        hashmap.delete('nonexistent_key')


def test_djb2_hash():
    assert djb2('test') == 6385723493


def test_sdbm_hash():
    assert sdbm('test') == 32745785343201586


def test_lose_lose_hash():
    assert lose_lose('test') == 448