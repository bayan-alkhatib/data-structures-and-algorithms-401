from stack_queue_brackets import __version__
from stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_version():
    assert __version__ == '0.1.0'


def test_validate_bracket1():
    actual=validate_brackets('{}(){}')
    expected=True
    assert actual==expected

def test_validate_bracket2():
    actual=validate_brackets('()[[Extra Characters]]')
    expected=True
    assert actual==expected

def test_validate_bracket3():
    actual=validate_brackets('[({}]')
    expected=False
    assert actual==expected

def test_validate_bracket4():
    actual=validate_brackets('{(})')
    expected=False
    assert actual==expected


