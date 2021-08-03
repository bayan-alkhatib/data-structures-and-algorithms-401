from graph import __version__

from graph.graph import Graph, Node, Edge

import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_add_node_successfully(graph_ins):
    expected=[key.value for key in graph_ins[0].adjacency_list]
    actual= [1,2,'bayan']

    assert expected == actual

    

def test_add_edge_successfully(graph_ins):
    expected_bayan=[1,2]
    b_values=graph_ins[0].adjacency_list[graph_ins[1]]
    actual_bayan=[item.node.value for item in b_values]

    expected_1=[2]
    values_1=graph_ins[0].adjacency_list[graph_ins[2]]
    actual_1=[values_1[0].node.value]

    assert expected_bayan==actual_bayan
    assert expected_1==actual_1



def test_get_nodes(graph_ins):
    actual=graph_ins[0].get_nodes()
    expected=[1, 2, 'bayan']
    assert actual == expected
   

def test_get_neighbors(graph_ins):
    actual=graph_ins[0].get_neighbors(graph_ins[1])
    expected=[(1, 0), (2, 0)]
    assert actual == expected

def test_neighbors_returned_with_weight(graph_2):
    expected=[('b',5), ('c',7)]
    actual=graph_2[0].get_neighbors(graph_2[1])

    assert expected == actual

def test_graph_size(graph_ins):
    actual= graph_ins[0].size()
    expected= 3
    assert actual==expected

def test_graph_with_1node_1edge():
    graph = Graph()
    a = graph.add_node('a')
    graph.add_edge(a,a)
    
    actual=(graph.get_nodes(),graph.get_neighbors(a))
    expected=  (['a'], [('a', 0)])
    assert actual==expected

def test_empty_graph():
    graph = Graph()
    actual=graph.size()
    expected= 0
    assert actual == expected 


@pytest.fixture
def graph_ins():
    graph= Graph()
    one= graph.add_node(1)
    two= graph.add_node(2)
    bayan= graph.add_node('bayan')

    graph.add_edge(bayan, one)
    graph.add_edge(bayan, two)

    graph.add_edge(one,two)

    return graph, bayan, one


@pytest.fixture
def graph_2():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a,b,5)
    graph.add_edge(a,c,7)

    return graph, a