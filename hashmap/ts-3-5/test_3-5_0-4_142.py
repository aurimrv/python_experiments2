import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

class TestHashMap:

    def test_insert_new_key(self):
        hm = HashMap()
        hm.insert('key1', 'value1')
        assert hm.get('key1') == 'value1'

    def test_insert_existing_key(self):
        hm = HashMap()
        hm.insert('key2', 'value2')
        hm.insert('key2', 'updated_value')
        assert hm.get('key2') == 'updated_value'

    def test_get_key_not_found(self):
        hm = HashMap()
        with pytest.raises(KeyError):
            hm.get('non_existent_key')

    def test_delete_existing_key(self):
        hm = HashMap()
        hm.insert('key3', 'value3')
        deleted_value = hm.delete('key3')
        assert deleted_value == ('key3', 'value3')
        with pytest.raises(KeyError):
            hm.get('key3')

    def test_delete_key_not_found(self):
        hm = HashMap()
        with pytest.raises(KeyError):
            hm.delete('non_existent_key')

class TestHashFunctions:

    def test_djb2(self):
        assert djb2('test_key') == 7572963594076045

    def test_sdbm(self):
        assert sdbm('test_key') == 606379187146086983188292032049998418

    def test_lose_lose(self):
        assert lose_lose('test_key') == 872