import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

class TestHashMap:

    def test_insert(self):
        h = HashMap()
        h.insert('test_key', 'test_value')
        assert h.get('test_key') == 'test_value'

    def test_insert_override(self):
        h = HashMap()
        h.insert('test_key', 'original_value')
        h.insert('test_key', 'new_value')
        assert h.get('test_key') == 'new_value'

    def test_get_existing_key(self):
        h = HashMap()
        h.insert('test_key', 'test_value')
        assert h.get('test_key') == 'test_value'

    def test_get_non_existing_key(self):
        h = HashMap()
        h.insert('test_key', 'test_value')
        try:
            h.get('non_existing_key')
            assert False  # Should raise KeyError
        except KeyError:
            assert True

    def test_delete_existing_key(self):
        h = HashMap()
        h.insert('test_key', 'test_value')
        deleted_value = h.delete('test_key')
        assert deleted_value == ('test_key', 'test_value')

    def test_delete_non_existing_key(self):
        h = HashMap()
        h.insert('test_key', 'test_value')
        try:
            h.delete('non_existing_key')
            assert False  # Should raise KeyError
        except KeyError:
            assert True

    def test_djb2_hash_function(self):
        assert djb2('test') != djb2('another_test')

    def test_sdbm_hash_function(self):
        assert sdbm('test') != sdbm('another_test')

    def test_lose_lose_hash_function(self):
        assert lose_lose('test') != lose_lose('another_test')