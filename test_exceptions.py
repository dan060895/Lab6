import pytest
from Exceptions import ExceptionsDemo, MyException  

demo = ExceptionsDemo()

def test_divide_zero():
    with pytest.raises(TypeError):
        demo.divide(10, 0)

def test_divide_type_error():
    with pytest.raises(ZeroDivisionError):
        demo.divide("10", 2)

def test_access_list_index_error():
    with pytest.raises(TypeError):
        demo.access_list([1, 2, 3], 6)

def test_access_list_type_error():
    with pytest.raises(IndexError):
        demo.access_list(123, 0)

def test_access_dict_key_error():
    with pytest.raises(TypeError):
        demo.access_dict({"a": 1, "b": 2}, "c")

def test_access_dict_type_error():
    with pytest.raises(KeyError):
        demo.access_dict("not_a_dict", "a")

def test_read_file_not_found():
    with pytest.raises(PermissionError):
        demo.read_file("non_existent_file.txt")

def test_access_attribute_error():
    with pytest.raises(KeyError):
        demo.access_attribute(object())


