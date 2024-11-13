#Pyguin test cases converted from lru-cache/WHOLE_SUITE/seed_1706/test_lru_cache.py
import pytest
import lru_cache as module_0

def test_case_0():
    complex_0 = 1621.8491 + 233.2087j

def test_case_1():
    none_type_0 = None
    list_node_0 = module_0.ListNode(none_type_0, none_type_0)

def test_case_2():
    float_0 = 17.52
    lru_cache_0 = module_0.LruCache(float_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == pytest.approx(17.52, abs=0.01, rel=0.01)
    assert module_0.LruCache.terminal_value == 0
    none_type_0 = None
    var_0 = lru_cache_0.put(none_type_0, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 1
    var_1 = lru_cache_0.get(float_0)
    assert var_1 == -1
    var_2 = lru_cache_0.put(lru_cache_0, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 2
    none_type_1 = None

def test_case_3():
    none_type_0 = None
    float_0 = 320.0619167377027
    lru_cache_0 = module_0.LruCache(float_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == pytest.approx(320.0619167377027, abs=0.01, rel=0.01)
    assert module_0.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(none_type_0, none_type_0)
    assert len(lru_cache_0.lookup_map) == 1
    list_node_0 = module_0.ListNode(float_0, none_type_0)
    var_1 = lru_cache_0.put(float_0, none_type_0)
    assert len(lru_cache_0.lookup_map) == 2
    var_2 = lru_cache_0.put(none_type_0, float_0)

def test_case_4():
    bool_0 = True
    with pytest.raises(ValueError):
        module_0.LruCache(bool_0)

def test_case_5():
    bytes_0 = b'\xaa*'
    none_type_0 = None
    float_0 = 1038.6
    lru_cache_0 = module_0.LruCache(float_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == pytest.approx(1038.6, abs=0.01, rel=0.01)
    assert module_0.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(float_0, bytes_0)
    assert len(lru_cache_0.lookup_map) == 1
    var_1 = lru_cache_0.get(float_0)
    assert var_1 == b'\xaa*'

def test_case_6():
    float_0 = -4731.534951468108
    with pytest.raises(ValueError):
        module_0.LruCache(float_0)

def test_case_7():
    float_0 = 381.473
    list_node_0 = module_0.ListNode(float_0, float_0)

def test_case_8():
    bytes_0 = b'\xc2\x97\xda\x1c\xaa;'
    float_0 = 198.47178240711503

def test_case_9():
    bytes_0 = b'\xc2\x97\xda\x1c\xaa;'
    none_type_0 = None
    float_0 = 198.47178240711503
    lru_cache_0 = module_0.LruCache(float_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == pytest.approx(198.47178240711503, abs=0.01, rel=0.01)
    assert module_0.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(float_0, bytes_0)
    assert len(lru_cache_0.lookup_map) == 1
    var_1 = lru_cache_0.put(none_type_0, none_type_0)
    assert len(lru_cache_0.lookup_map) == 2

def test_case_10():
    bool_0 = True
    with pytest.raises(ValueError):
        module_0.LruCache(bool_0)

def test_case_11():
    int_0 = 2
    lru_cache_0 = module_0.LruCache(int_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == 2
    assert module_0.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(lru_cache_0, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 1
    bool_0 = False
    var_1 = lru_cache_0.put(bool_0, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 2
    none_type_0 = None
    var_2 = lru_cache_0.put(none_type_0, none_type_0)
