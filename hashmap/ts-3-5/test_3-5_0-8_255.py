import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(module_dir, '..'))
sys.path.append(project_dir)

from hash_map import HashMap, djb2, sdbm, lose_lose

import pytest

class TestHashMap:

    def test_insert(self):
        h = HashMap()
        h.insert(1, 'apple')
        assert h.get(1) == 'apple'

    def test_insert_override(self):
        h = HashMap()
        h.insert(1, 'apple')
        h.insert(1, 'banana')
        assert h.get(1) == 'banana'

    def test_get(self):
        h = HashMap()
        h.insert(1, 'apple')
        assert h.get(1) == 'apple'

    def test_get_key_error(self):
        h = HashMap()
        with pytest.raises(KeyError):
            h.get(1)

    def test_delete(self):
        h = HashMap()
        h.insert(1, 'apple')
        deleted = h.delete(1)
        assert deleted == (1, 'apple')

    def test_delete_key_error(self):
        h = HashMap()
        with pytest.raises(KeyError):
            h.delete(1)

class TestHashFunctions:

    def test_djb2(self):
        assert djb2('test') == 6385723493

    def test_sdbm(self):
        assert sdbm('test') == 32745785343201586

    def test_lose_lose(self):
        assert lose_lose('test') == 448