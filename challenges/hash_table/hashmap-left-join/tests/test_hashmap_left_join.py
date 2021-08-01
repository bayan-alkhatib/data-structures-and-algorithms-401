from typing import Hashable
from hashmap_left_join import __version__
from hashmap_left_join.hash_map_left_join import left_join
import sys
sys.path.append("/home/bayan/code-401/data-structures-and-algorithms-401/data-structures/hashtable")
from hashtable.hashtable import Hashtable

import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_success(hash_1):
    actual=left_join(hash_1[0], hash_1[1])
    expected= [['wrath', 'anger', 'delight'],
               ['wrath', 'anger', 'delight'],
               ['outift', 'garb', None],
               ['diligent', 'employed', 'idle'],
               ['guide', 'usher', 'follow'],
               ['fond', 'enamored', 'averse'],
               ]
    assert expected == actual


def test_ht1_empty():
    ht1=Hashtable()
    ht2=Hashtable()

    ht2.add('fond','averse')
    ht2.add('wrath','delight')
    ht2.add('diligent','idle')
    ht2.add('guide','follow')
    ht2.add('flow','jam')

    actual=left_join(ht1,ht2)
    expected='cant joint left table is empty'
    assert expected == actual


def test_ht2_empty():
    ht1=Hashtable()
    ht2=Hashtable()

    ht1.add('fond','enamored')
    ht1.add('wrath','anger')
    ht1.add('diligent','employed')
    ht1.add('outift','garb')
    ht1.add('guide','usher')

    actual=left_join(ht1,ht2)
    expected= [ ['wrath', 'anger', None],
                ['outift', 'garb', None],
                ['diligent', 'employed', None],
                ['guide', 'usher', None],
                ['fond', 'enamored', None],
               ]
    assert expected == actual






@pytest.fixture
def hash_1():
    ht1 = Hashtable()
    ht2 = Hashtable()

    ht1.add('fond','enamored')
    ht1.add('wrath','anger')
    ht1.add('wrath','anger')
    ht1.add('diligent','employed')
    ht1.add('outift','garb')
    ht1.add('guide','usher')


    ht2.add('fond','averse')
    ht2.add('wrath','delight')
    ht2.add('diligent','idle')
    ht2.add('guide','follow')
    ht2.add('flow','jam')

    return ht1, ht2

