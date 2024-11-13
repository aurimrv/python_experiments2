#Pyguin test cases converted from graph2/MOSA/seed_1706/test_graph2.py
import pytest
import graph2 as module_0

def test_case_0():
    int_0 = -1519
    str_0 = '=@@\x0cQ$U'
    graph_0 = module_0.Graph(str_0)
    assert graph_0.graph == {'=': {*()}, '@': {*()}, '\x0c': {*()}, 'Q': {*()}, '$': {*()}, 'U': {*()}}

def test_case_1():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}

def test_case_2():
    none_type_0 = None
    graph_0 = module_0.Graph(none_type_0)
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.add_edge(none_type_0, none_type_0)
    var_1 = graph_0.edges()

def test_case_3():
    float_0 = 2003.334
    list_0 = [float_0, float_0]
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.edges()

def test_case_4():
    float_0 = -412.0
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.nodes()
    none_type_0 = None
    graph_1 = module_0.Graph()
    var_1 = graph_1.add_node(float_0)

def test_case_5():
    none_type_0 = None
    graph_0 = module_0.Graph(none_type_0)
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.add_node(graph_0)

def test_case_6():
    float_0 = 2003.0
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    graph_1 = graph_0.add_edge(float_0, graph_0)

def test_case_7():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}

def test_case_8():
    none_type_0 = None
    graph_0 = module_0.Graph(none_type_0)
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.edges()
    str_0 = 'Ew'
    list_0 = [str_0, str_0]
    bool_0 = True
    tuple_0 = (list_0, bool_0)
    graph_1 = module_0.Graph()

def test_case_9():
    graph_0 = module_0.Graph()
    assert f'{type(graph_0).__module__}.{type(graph_0).__qualname__}' == 'graph2.Graph'
    assert graph_0.graph == {}
    var_0 = graph_0.add_edge(graph_0, graph_0)
    var_1 = graph_0.add_edge(var_0, graph_0)
    var_2 = graph_0.del_node(var_1)
