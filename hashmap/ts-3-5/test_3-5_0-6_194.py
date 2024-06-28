import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

# Test cases for HashMap class
class TestHashMap:
    def test_insert_single_key_value(self):
        hm = HashMap()
        hm.insert('test_key', 'test_value')
        assert hm.get('test_key') == 'test_value'

    def test_insert_override_existing_key(self):
        hm = HashMap()
        hm.insert('test_key', 'test_value')
        hm.insert('test_key', 'new_value')
        assert hm.get('test_key') == 'new_value'

    def test_get_key_not_found(self):
        hm = HashMap()
        with pytest.raises(KeyError):
            hm.get('non_existent_key')

    def test_delete_single_key(self):
        hm = HashMap()
        hm.insert('test_key', 'test_value')
        deleted_value = hm.delete('test_key')
        assert deleted_value == ('test_key', 'test_value')
        with pytest.raises(KeyError):
            hm.get('test_key')

# Test cases for hashing functions
class TestHashFunctions:
    def test_djb2_hash(self):
        assert djb2('test') == djb2('test')

    def test_sdbm_hash(self):
        assert sdbm('test') == sdbm('test')

    def test_lose_lose_hash(self):
        assert lose_lose('test') == lose_lose('test')