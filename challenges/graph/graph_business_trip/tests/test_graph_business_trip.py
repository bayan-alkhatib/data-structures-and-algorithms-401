from graph_business_trip import __version__
from graph_business_trip.graph_business_trip import business_trip
import sys 
sys.path.append('/home/bayan/code-401/data-structures-and-algorithms-401/data-structures/graph')

from graph.graph import  Graph



import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_success_1( map):
    cities=['amman','istanbol','london']
    actual= business_trip(map,cities)
    expected='True, $460'
    assert expected==actual

def test_success_2(map):
    cities=['dubai','london']
    actual= business_trip(map,cities)
    expected='True, $360'
    assert expected==actual

def test_one_of_cities_not_in_map(map):
    cities=['dubai','paris']
    actual= business_trip(map,cities)
    expected=False
    assert expected==actual

def test_no_road_btw_cities(map):
    cities=['dubai','london','istanbol']
    actual= business_trip(map,cities)
    expected=False
    assert expected==actual




@pytest.fixture
def map():
    graph =Graph()
    amman = graph.add_node('amman')
    istanbol = graph.add_node('istanbol')
    dubai = graph.add_node('dubai')
    london= graph.add_node('london')

    graph.add_edge(amman,istanbol,250)
    graph.add_edge(amman,dubai,180)
    graph.add_edge(dubai,london,360)
    graph.add_edge(istanbol,london, 210)

    return graph