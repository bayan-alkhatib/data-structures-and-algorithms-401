from trees import __version__
from trees.trees import  Binary_Tree, Node

import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_instantiate_an_empty_tree():
    pass

def  test_instantiate_tree_single_root_node():
    pass

def test_add_left_child_right_child_single_root():
    pass

def test_collection_from_preorder_traversal():
    pass

def test_collection_from_inorder_traversal():
    pass

def collection_from_postorder_traversal():
    pass

@pytest.fixture
def tree_instance():
    pass

