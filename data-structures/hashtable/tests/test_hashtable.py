from hashtable import __version__
from hashtable.hashtable import Hashtable
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_Add_to_hashtable(hashtable_instance):
   hash=hashtable_instance.hash('name')
   actual= hashtable_instance.buckets[hash].head.value
   expected={'name':'bayan'}
   assert actual==expected
   

def test_get_value_from_key(hashtable_instance):
    actual=hashtable_instance.get('name')
    expected='bayan'
    assert actual==expected
    

def test_key_that_does_not_exist(hashtable_instance):
    actual=hashtable_instance.contains('phone')
    expected=False
    assert actual==expected

def test_Successfully_handle_collision(hashtable_instance):
   hash=hashtable_instance.hash('name')
   actual= [hashtable_instance.buckets[hash].head.value,hashtable_instance.buckets[hash].head.next.value]
   expected=[{'name':'bayan'},{'mane':'no thing'}]
   assert actual==expected
    

def test_retrieve_value_from_bucket_has_collision(hashtable_instance):
    actual=hashtable_instance.get('name')
    expected='bayan'
    assert actual==expected

def  test_hash_key_to_in_range_value(hashtable_instance):
    actual=hashtable_instance.hash('phone')
    expected=1006
    assert actual==expected
    


@pytest.fixture
def hashtable_instance():
   h_table=Hashtable()
   h_table.add('name','bayan')
   h_table.add('mane','no thing')
   return h_table

