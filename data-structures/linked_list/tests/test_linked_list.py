from linked_list import __version__


from linked_list.linked_list import (
    Node,
    LinkedList
)

def test_version():
    assert __version__ == '0.1.0'

def test_instantiate_empty_linked_list():
    lnk_lst=LinkedList()
    expected="NULL"
    actual=lnk_lst.__str__()
    assert expected==actual

def test_insert_into_linked_list():
    new_list=LinkedList()
    excepted= 4
    actual= new_list.insert(4)
    assert excepted==actual

def test_head_point_to_first_node():
    lnk_lst=LinkedList()
    excepted=None
    actual= lnk_lst.head
    assert excepted==actual


def test_insert_multiple_nodes():
    lnk_lst=LinkedList()
    lnk_lst.insert(1)
    lnk_lst.insert('a')
    lnk_lst.insert(6)
    excepted="{4} -> {1} -> {a} -> {6} -> NULL"
    actual= lnk_lst.__str__()
    assert excepted==actual

def test_finding_value_within_linked_list():
    lnk_lst=LinkedList()
    excepted=True
    actual= lnk_lst.include(6)
    assert excepted==actual

def test_not_finding_value_within_linked_list():
    lnk_lst=LinkedList()
    excepted=False
    actual= lnk_lst.include('b')
    assert excepted==actual

def test_collection_of_values_in_linked_list():
    lnk_lst=LinkedList()
    excepted="{4} -> {1} -> {a} -> {6} -> NULL"
    actual= lnk_lst.__str__()
    assert excepted==actual
    