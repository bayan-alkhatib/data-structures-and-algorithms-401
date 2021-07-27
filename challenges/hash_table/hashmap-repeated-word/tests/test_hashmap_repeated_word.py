from hashmap_repeated_word import __version__
from hashmap_repeated_word.hashmap_repeated_word import repeated_word

def test_version():
    assert __version__ == '0.1.0'

def test_word_dupicate():
    str='Once upon a time, there was a brave princess who.'
    actual=repeated_word(str)
    expected='a'
    assert actual==expected


def test_word_dupicate_2():
    str='It was a queer, sultry summer, the summer they electrocuted the Rosenbergs'
    actual=repeated_word(str)
    expected='summer'
    assert actual==expected

def test_word_no_dupicate():
    str='one day you will look back and laugh on the past'
    actual=repeated_word(str)
    expected='this string has no duplicates'
    assert actual==expected

def test_word_empty_string():
    str=''
    actual=repeated_word(str)
    expected='this string is empty'
    assert actual==expected