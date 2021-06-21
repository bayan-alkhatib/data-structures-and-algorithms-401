from queue_with_stacks import __version__
from queue_with_stacks.queue_with_stacks import PseudoQueue
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_enqueue_to_psudeo_queue(psudeo_queue):
    expected=5
    actual= psudeo_queue.rear.top.value
    assert expected==actual


def test_enqueue_None_value():
    p_queue=PseudoQueue()
    expected=False
    actual=p_queue.enqueue(None)
    assert expected==actual

def test_dequeue_from_psudeo_queue(psudeo1_queue):
    expected=7
    actual=psudeo1_queue.dequeue()
    assert expected==actual



@pytest.fixture
def psudeo_queue():
    p_queue=PseudoQueue()
    p_queue.enqueue(5)
    return p_queue


@pytest.fixture
def psudeo1_queue():
    p_queue=PseudoQueue()
    p_queue.enqueue(7)
    p_queue.enqueue(4)
    p_queue.dequeue()
    return p_queue