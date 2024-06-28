import os
import sys
import pytest

module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

class TestHashMap:

    @pytest.fixture
    def hashmap(self):
        return HashMap()

    def test_insert_and_get(self, hashmap):
        hashmap.insert('key1', 'value1')
        assert hashmap.get('key1') == 'value1'

    def test_insert_override(self, hashmap):
        hashmap.insert('key2', 'value2')
        hashmap.insert('key2', 'new_value2')
        assert hashmap.get('key2') == 'new_value2'

    def test_delete(self, hashmap):
        hashmap.insert('key3', 'value3')
        assert hashmap.delete('key3') == ('key3', 'value3')
        with pytest.raises(KeyError):
            hashmap.get('key3')

class TestHashFunctions:

    def test_djb2(self):
        assert djb2('test') == 6385723493

    def test_sdbm(self):
        assert sdbm('test') == 32745785343201586

    def test_lose_lose(self):
        assert lose_lose('test') == 448