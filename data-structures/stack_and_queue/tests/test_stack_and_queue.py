from stack_and_queue import __version__

from stack_and_queue.stack_and_queue import Queue, Stack

import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_push_onto_a_stack(stack_instance):
    actual=stack_instance.push(4)
    expected=4
    assert actual==expected
    

def test_push_multiple_values_onto_stack(stack_instance):
    actual=stack_instance.top.value
    expected=8
    assert actual==expected
    

def test_pop_off_the_stack(stack2_instance):
    actual=stack2_instance.top.value
    expected=4
    assert actual==expected
    

def test_empty_stack_after_multiple_pops(stack3_instance):
    actual=stack3_instance.top
    expected=None
    assert actual==expected

def test_peek_next_item_on_the_stack(stack_instance):
    actual=stack_instance.top.next.value
    expected=4
    assert actual==expected

def test_instantiate_empty_stack():
    stack=Stack()
    actual=stack.top
    expected=None
    assert actual==expected


def test_pop_or_peek_empty_stack():
    stack=Stack()
    actual= stack.pop() or stack.peek()
    expected='Error!'
    assert actual==expected

def test_enqueue_into_queue(queue_instance):
    actual= queue_instance.enqueue(4)
    expected=4
    assert actual==expected


def test_enqueue_multiple_values_to_queue(queue_instance):
    actual= queue_instance.rear.value
    expected='bayan'
    assert actual==expected


def test_dequeue_out_of_queue(queue2_instance):
    actual=queue2_instance.front.value
    expected='bayan'
    assert actual==expected


def test_peek_into_queue(queue_instance):
    actual=queue_instance.front.value
    expected=4
    assert actual==expected

def test_empty_queue_after_multiple_dequeues(queue3_instance):
    actual=queue3_instance.front
    expected=None
    assert actual==expected

def test_instantiate_empty_queue():
    queue=Queue()
    actual=queue.front
    expected=None
    assert expected==actual

def test_dequeue_or_peek_empty_queue():
    queue=Queue()
    actual=queue.peek() or queue.dequeue()
    excepted='Error!'
    assert excepted==actual

@pytest.fixture
def stack_instance():
    stack=Stack()
    stack.push(4)
    stack.push(8)
    return stack

@pytest.fixture
def stack2_instance():
    stack_pop=Stack()
    stack_pop.push(4)
    stack_pop.push(8)
    stack_pop.pop()
    return stack_pop

@pytest.fixture
def stack3_instance():
    stack=Stack()
    stack.push(4)
    stack.push(8)
    stack.pop()  
    stack.pop()
    return stack

@pytest.fixture
def queue_instance():
    queue=Queue()
    queue.enqueue(4)
    queue.enqueue('bayan')
    return queue

@pytest.fixture
def queue2_instance():
    queue=Queue()
    queue.enqueue(4)
    queue.enqueue('bayan')
    queue.dequeue()
    return queue

@pytest.fixture
def queue3_instance():
    queue=Queue()
    queue.enqueue(4)
    queue.enqueue('bayan')
    queue.dequeue()
    queue.dequeue()
    return queue