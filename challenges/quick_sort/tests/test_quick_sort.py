from quick_sort import __version__
from quick_sort.quick_sort import quick_sort

def test_version():
    assert __version__ == '0.1.0'


def test_success_sort():
    array=[75,15,6,2,8,3]
    actual=quick_sort(array,0,5)
    expected=[2,3,6,8,15,75]
    assert actual==expected

def test_Reverse_sort():
    array=[20,18,12,8,5,-2]
    actual=quick_sort(array,0,5)
    expected=[-2,5,8,12,18,20]
    assert actual==expected

def test_few_uniques_sort():
    array=[5,12,7,5,5,7]
    actual=quick_sort(array,0,5)
    expected=[5,5,5,7,7,12]
    assert actual==expected

def test_nearly_sorted_sort():
    array=[2,3,5,7,13,11]
    actual=quick_sort(array,0,5)
    expected=[2,3,5,7,11,13]
    assert actual==expected
