#Pyguin test cases converted from graph2/WHOLE_SUITE/seed_1706/test_graph2.py
import pytest
import graph2 as module_0

def test_case_0():
    pass

def test_case_1():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    bool_0 = True
    bool_1 = True
    list_0 = [bool_1, bool_1]
    none_type_0 = None
    var_0 = graph_0.edges()
    var_1 = graph_0.has_node(none_type_0)
    assert var_1 is False

def test_case_2():
    list_0 = []
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.edges()

def test_case_3():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.nodes()
    var_1 = graph_0.has_node(graph_0)
    assert var_1 is False

def test_case_4():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    none_type_0 = None
    var_0 = graph_0.add_node(none_type_0)
    var_1 = graph_0.add_node(graph_0)
    var_2 = graph_0.del_node(none_type_0)

def test_case_5():
    int_0 = 3801
    set_0 = {int_0, int_0, int_0, int_0}
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}

def test_case_6():
    str_0 = '\nl7vR-\tt>fm1d,uq('
    complex_0 = 4055 - 1344j
    str_1 = '=@@\x0cQ$U'
    graph_0 = module_0.Graph(str_1)
    assert graph_0.graph == {'=': {*()}, '@': {*()}, '\x0c': {*()}, 'Q': {*()}, '$': {*()}, 'U': {*()}}
    var_0 = graph_0.add_edge(complex_0, str_0)
    assert graph_0.graph == {'=': {*()}, '@': {*()}, '\x0c': {*()}, 'Q': {*()}, '$': {*()}, 'U': {*()}, 4055 - 1344j: {'\nl7vR-\tt>fm1d,uq('}, '\nl7vR-\tt>fm1d,uq(': {*()}}
    var_1 = graph_0.edges()

def test_case_7():
    int_0 = 991
    float_0 = 1076.4163
    bytes_0 = b'\xdd\xb6\xe8\x96\x8e\x80CMc\xe5\xcf\x14'
    none_type_0 = None
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.add_edge(int_0, float_0)
    graph_1 = module_0.Graph(none_type_0)
