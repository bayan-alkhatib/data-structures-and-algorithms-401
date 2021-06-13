from linked_list import __version__
from linked_list import linked_list

from linked_list.linked_list import (
    Node,
    LinkedList
)

def test_version():
    assert __version__ == '0.1.0'

def test_instantiate_empty_linked_list():
    expected='LinkedList.str'
    actual=LinkedList()
    assert expected==actual

def test_insert_into_linked_list():
    new_list=LinkedList()
    excepted=Node(4)
    actual= new_list.insert(4)
    assert excepted==actual

def test_head_point_to_first_node():
    pass

def test_insert_multiple_nodes():
    pass

def test_finding_value_within_linked_list():
    LinkList=LinkedList(5)
    excepted=True
    actual= LinkList.include()
    assert excepted==actual

def test_not_finding_value_within_linked_list():
    LinkList=LinkedList(7)
    excepted=False
    actual= LinkList.include()
    assert excepted==actual

def test_collection_of_values_in_linked_list():
    LinkList = LinkedList()
    LinkList.append(1)
    LinkList.append(2)
    LinkList.append(3)
    actual = LinkedList.__str__
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> None'

