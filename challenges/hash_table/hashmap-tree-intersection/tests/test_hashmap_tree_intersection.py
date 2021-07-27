from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.hashmap_tree_intersection import tree_intersection

import sys
import pytest

sys.path.append("/home/bayan/code-401/data-structures-and-algorithms-401/data-structures/trees")
from trees.trees import Binary_Search_Tree


def test_version():
    assert __version__ == '0.1.0'

def test_success1(tree_1):
    actual= tree_intersection(tree_1[0],tree_1[1])
    expected=[100,5,250]
    assert actual == expected


def test_success2(tree_2):
    actual= tree_intersection(tree_2[0],tree_2[1])
    expected=[50,27,68]
    assert actual == expected


def test_tree_empty():
    bt1=Binary_Search_Tree()
    bt2=Binary_Search_Tree()
    actual= tree_intersection(bt1,bt2)
    expected='input tree is empty'
    assert actual == expected

def test_tree_no_intersection(tree_3):
    actual= tree_intersection(tree_3[0],tree_3[1])
    expected='input Trees have No intersection'
    assert actual == expected


@pytest.fixture
def tree_1():
    bt1=Binary_Search_Tree()
    bt1.add(100)
    bt1.add(85)
    bt1.add(5)
    bt1.add(306)
    bt1.add(16)
    bt1.add(250)

    bt2=Binary_Search_Tree()
    bt2.add(100)
    bt2.add(50)
    bt2.add(200)
    bt2.add(5)
    bt2.add(13)
    bt2.add(250)
    return bt1,bt2

@pytest.fixture
def tree_2():
    bt1=Binary_Search_Tree()
    bt1.add(99)
    bt1.add(50)
    bt1.add(27)
    bt1.add(16)
    bt1.add(68)

    bt2=Binary_Search_Tree()
    bt2.add(100)
    bt2.add(50)
    bt2.add(27)
    bt2.add(13)
    bt2.add(68)
    return bt1,bt2

@pytest.fixture
def tree_3():
    bt1=Binary_Search_Tree()
    bt1.add(48)
    bt1.add(50)
    bt1.add(27)
    bt1.add(16)
    bt1.add(68)

    bt2=Binary_Search_Tree()
    bt2.add(101)
    bt2.add(51)
    bt2.add(28)
    bt2.add(13)
    bt2.add(69)
    return bt1,bt2


