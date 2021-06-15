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
    actual=lnk_lst.head
    assert excepted==actual


def test_insert_multiple_nodes():
    lnk_lst=LinkedList()
    lnk_lst.insert(1)
    lnk_lst.insert('a')
    lnk_lst.insert(6)
    excepted="{6} -> {a} -> {1} -> NULL"
    actual= lnk_lst.__str__()
    assert excepted==actual

def test_finding_value_within_linked_list():
    lnk_lst=LinkedList()
    lnk_lst.insert(6)
    excepted=True
    actual=lnk_lst.include(6)
    assert excepted==actual

def test_not_finding_value_within_linked_list():
    lnk_lst=LinkedList()
    excepted=False
    actual= lnk_lst.include('b')
    assert excepted==actual

def test_add_node_to_end_of_linked_list():
    lnk_lst=LinkedList()
    excepted=8
    actual=lnk_lst.append(8)
    assert excepted==actual

def test_add_multiple_nodes_to_end_of_linked_list():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.append('b')
    excepted='{8} -> {3} -> {b} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual

def test_insert_node_before_node_middle_of_linked_list():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.append('b')
    lnk_lst.append('4')
    lnk_lst.insert_before('b',7)
    excepted='{8} -> {3} -> {7} -> {b} -> {4} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual


def test_insert_node_before_the_first_node():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.insert_before(8,'a')
    excepted='{a} -> {8} -> {3} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual

def test_insert_after_node_middle_of_linked_list():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.append('b')
    lnk_lst.append('4')
    lnk_lst.insert_after('b',7)
    excepted='{8} -> {3} -> {b} -> {7} -> {4} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual

def test_insert_node_after_last_node():
    lnk_lst=LinkedList()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.insert_after(8,'a')
    excepted='{8} -> {a} -> {3} -> NULL'
    actual=lnk_lst.__str__()
    assert excepted==actual


    