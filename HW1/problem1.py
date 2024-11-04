from typing import List


def get_min_max_rest(a: int, b: int, c: int) -> List[int]:
    arr = [a, b, c]
    arr.sort(reverse=True)
    return [arr[0], arr[-1], arr[1]]

def test_1():
    a, b, c = 8, 2, 14
    outp = get_min_max_rest(a,b,c)
    ans = [14, 2, 8]
    assert ans == outp, f"outp {outp} != {ans}"

def test_2():
    a, b, c = 23, 23, 21
    outp = get_min_max_rest(a,b,c)
    ans = [23, 21, 23]
    assert ans == outp, f"outp {outp} != {ans}"

def test_3():
    a, b, c = 1, 1, 1
    outp = get_min_max_rest(a,b,c)
    ans = [1, 1, 1]
    assert ans == outp, f"outp {outp} != {ans}"

def get_min_max_rest_formatted_outp(a: int, b: int, c: int) -> None:
    ans = get_min_max_rest(a, b, c)
    print(*ans, sep='\n')

a, b, c = 1, 2, 3
get_min_max_rest_formatted_outp(a, b, c)