import pytest
from lru_cache import LruCache

class TestLru:

    CONST_HELLO = 'hello'

    CONST_WORLD = 'world'

    CONST_HELLO_2 = 'hello 2'

    CONST_BAM = '!'

    def test_LRU_simple(self):
        cache = LruCache(2)

        cache.put(1, self.CONST_HELLO)

        assert cache.get(1) == self.CONST_HELLO

        cache.put(2, self.CONST_WORLD)

        assert cache.get(2) == self.CONST_WORLD

        cache.get(1)

        cache.put(3, self.CONST_BAM)

        assert cache.get(2) == -1

        cache.put(3, self.CONST_BAM)

    def test_LRU_bad_input(self):
        capacity = 0

        with pytest.raises(ValueError):
            LruCache(capacity)

