from typing import Union, TypeAlias
Number: TypeAlias = Union[float, int]


def has_pos_numb(arr: list) -> bool:
    return any(map(lambda x: isinstance(x, Number) and x > 0, arr))

def are_all_els_nums(arr: list) -> bool:
    return all(map(lambda x: isinstance(x, Number), arr))

def sort_arr(arr: list) -> list:
    return sorted(arr)

def program1(arr: list) -> list:
    assert isinstance(arr, list), 'inp must be a list'
    assert has_pos_numb(arr)
    assert sort_arr(arr)
    return sort_arr(arr)

def test_1():
    x = [1, 3, 5]
    assert has_pos_numb(x) == True
    x = [-2, 0, -1]
    assert has_pos_numb(x) == False
    x = ['t', 'f']
    assert has_pos_numb(x) == False

def test_2():
    x = [1, 2, 3]
    assert are_all_els_nums(x) == True
    x = [1, 'f', '3']
    assert are_all_els_nums(x) == False

def test_3():
    x = [2 ,1, -3, 3]
    assert sort_arr(x) == [-3, 1, 2, 3]


x = [1,2, -5, 5]
print(program1(x))