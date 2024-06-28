import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

class TestHashMap:
    def test_insert_single_value(self):
        hm = HashMap()
        hm.insert('test_key', 'test_value')
        assert hm.get('test_key') == 'test_value'

    def test_insert_duplicate_key(self):
        hm = HashMap()
        hm.insert('test_key', 'original_value')
        hm.insert('test_key', 'new_value')
        assert hm.get('test_key') == 'new_value'

    def test_get_nonexistent_key(self):
        hm = HashMap()
        with pytest.raises(KeyError):
            hm.get('nonexistent_key')

    def test_delete_existing_key(self):
        hm = HashMap()
        hm.insert('test_key', 'test_value')
        deleted_val = hm.delete('test_key')
        assert deleted_val == ('test_key', 'test_value')
        with pytest.raises(KeyError):
            hm.get('test_key')

    def test_delete_nonexistent_key(self):
        hm = HashMap()
        with pytest.raises(KeyError):
            hm.delete('nonexistent_key')

class TestHashFunctions:
    def test_djb2_happy_path(self):
        assert djb2('test_key') == 7572963594076045

    def test_sdbm_happy_path(self):
        assert sdbm('test_key') == 606379187146086983188292032049998418

    def test_lose_lose_happy_path(self):
        assert lose_lose('test_key') == 872

    def test_djb2_empty_key(self):
        assert djb2('') == 5381

    def test_sdbm_empty_key(self):
        assert sdbm('') == 0

    def test_lose_lose_empty_key(self):
        assert lose_lose('') == 0