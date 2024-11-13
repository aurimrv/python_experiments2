#Pyguin test cases converted from lru-cache/MOSA/seed_1706/test_lru_cache.py
import pytest
import builtins as module_0
import lru_cache as module_1

def test_case_0():
    list_0 = []
    object_0 = module_0.object(*list_0)
    bool_0 = False
    with pytest.raises(ValueError):
        module_1.LruCache(bool_0)

def test_case_1():
    none_type_0 = None
    list_node_0 = module_1.ListNode(none_type_0, none_type_0)
    int_0 = 351
    list_node_1 = module_1.ListNode(int_0, int_0)
    lru_cache_0 = module_1.LruCache(int_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == 351
    assert module_1.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(int_0, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 1

def test_case_2():
    none_type_0 = None

def test_case_3():
    float_0 = 237.76570221028499
    none_type_0 = None
    lru_cache_0 = module_1.LruCache(float_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == pytest.approx(237.76570221028499, abs=0.01, rel=0.01)
    assert module_1.LruCache.terminal_value == 0
    object_0 = module_0.object()
    int_0 = 1286
    var_0 = lru_cache_0.put(int_0, object_0)
    assert len(lru_cache_0.lookup_map) == 1
    var_1 = lru_cache_0.put(float_0, float_0)
    assert len(lru_cache_0.lookup_map) == 2
    list_node_0 = module_1.ListNode(var_0, float_0)
    var_2 = lru_cache_0.get(none_type_0)
    assert var_2 == -1

def test_case_4():
    float_0 = 196.2154521408226
    lru_cache_0 = module_1.LruCache(float_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == pytest.approx(196.2154521408226, abs=0.01, rel=0.01)
    assert module_1.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(lru_cache_0, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 1
    lru_cache_1 = module_1.LruCache(float_0)
    object_0 = module_0.object()
    var_1 = lru_cache_0.get(lru_cache_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(var_1.head).__module__}.{type(var_1.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(var_1.tail).__module__}.{type(var_1.tail).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(var_1.lookup_map).__module__}.{type(var_1.lookup_map).__qualname__}' == 'builtins.dict'
    assert len(var_1.lookup_map) == 1
    assert var_1.capacity == pytest.approx(196.2154521408226, abs=0.01, rel=0.01)
    var_2 = lru_cache_1.put(lru_cache_1, lru_cache_1)
    assert len(lru_cache_1.lookup_map) == 1
    var_3 = var_1.put(var_2, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 2
    assert len(var_1.lookup_map) == 2
    var_4 = lru_cache_1.put(float_0, float_0)
    var_5 = lru_cache_1.put(var_4, var_2)
    var_6 = lru_cache_0.get(var_5)
    var_7 = lru_cache_1.put(var_3, var_1)

def test_case_5():
    int_0 = 5
    lru_cache_0 = module_1.LruCache(int_0)
    assert f'{type(lru_cache_0).__module__}.{type(lru_cache_0).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(lru_cache_0.head).__module__}.{type(lru_cache_0.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(lru_cache_0.tail).__module__}.{type(lru_cache_0.tail).__qualname__}' == 'lru_cache.ListNode'
    assert lru_cache_0.lookup_map == {}
    assert lru_cache_0.capacity == 5
    assert module_1.LruCache.terminal_value == 0
    var_0 = lru_cache_0.put(int_0, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 1
    none_type_0 = None
    var_1 = lru_cache_0.put(none_type_0, lru_cache_0)
    assert len(lru_cache_0.lookup_map) == 2
    bool_0 = True
    var_2 = lru_cache_0.put(bool_0, var_1)
    assert len(lru_cache_0.lookup_map) == 3
    float_0 = 196.2154521408226
    lru_cache_1 = module_1.LruCache(float_0)
    var_3 = lru_cache_0.get(lru_cache_1)
    assert var_3 == -1
    none_type_1 = None
    var_4 = lru_cache_1.get(none_type_1)
    assert var_4 == -1
    var_5 = lru_cache_1.put(lru_cache_1, lru_cache_1)
    assert len(lru_cache_1.lookup_map) == 1
    lru_cache_2 = module_1.LruCache(float_0)
    var_6 = lru_cache_1.get(lru_cache_1)
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'lru_cache.LruCache'
    assert f'{type(var_6.head).__module__}.{type(var_6.head).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(var_6.tail).__module__}.{type(var_6.tail).__qualname__}' == 'lru_cache.ListNode'
    assert f'{type(var_6.lookup_map).__module__}.{type(var_6.lookup_map).__qualname__}' == 'builtins.dict'
    assert len(var_6.lookup_map) == 1
    assert var_6.capacity == pytest.approx(196.2154521408226, abs=0.01, rel=0.01)
    var_7 = lru_cache_2.put(lru_cache_2, lru_cache_2)
    assert len(lru_cache_2.lookup_map) == 1
    bytes_0 = b'\x1c\x9a\xe7\x15\x9do\xd3\xcbh\x01Jd\xb3u[\xa1/'
    set_0 = set()
    list_node_0 = module_1.ListNode(var_2, set_0)
    list_node_1 = module_1.ListNode(bytes_0, var_6)
    assert f'{type(list_node_1.val).__module__}.{type(list_node_1.val).__qualname__}' == 'lru_cache.LruCache'
    var_8 = lru_cache_0.put(lru_cache_1, var_4)
    assert len(lru_cache_0.lookup_map) == 4
    tuple_0 = ()
    var_9 = lru_cache_0.put(tuple_0, list_node_1)
    assert len(lru_cache_0.lookup_map) == 5
    var_10 = lru_cache_0.put(var_4, bytes_0)
    list_node_2 = module_1.ListNode(int_0, none_type_1)
    var_11 = lru_cache_0.put(var_8, var_5)
