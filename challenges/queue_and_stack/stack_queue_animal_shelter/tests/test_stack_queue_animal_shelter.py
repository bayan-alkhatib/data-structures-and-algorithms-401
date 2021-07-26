from stack_queue_animal_shelter import __version__

from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter

import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_enqueue_to_AnimalShelter_dog(animalShelter_1):
    expected='Max'
    actual= animalShelter_1[1]
    assert expected==actual

def test_enqueue_to_AnimalShelter_cat(animalShelter_1):
    expected='Bella'
    actual= animalShelter_1[2]
    assert expected==actual


def test_enqueue_None_value():
    ani_shelter=AnimalShelter()
    expected=None
    actual= ani_shelter.enqueue('cooper','horse')
    assert expected==actual


def test_dequeue_to_AnimalShelter_dog(animalShelter_1):
    expected='Max'
    actual= animalShelter_1[3]
    assert expected==actual

def test_enqueue_to_AnimalShelter_cat(animalShelter_1):
    expected='Bella'
    actual= animalShelter_1[4]
    assert expected==actual


@pytest.fixture
def animalShelter_1():
    ani_shelter=AnimalShelter()
    dog_enq=ani_shelter.enqueue('Max','dog')
    cat_enq=ani_shelter.enqueue('Bella','cat')
    ani_shelter.enqueue('Buddy','dog')
    ani_shelter.enqueue('Lucy','cat')
    dog_deq=ani_shelter.dequeue('dog')
    cat_deq=ani_shelter.dequeue('cat')
    return ani_shelter, dog_enq, cat_enq, dog_deq, cat_deq



