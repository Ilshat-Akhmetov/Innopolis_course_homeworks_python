from typing import Iterable

class CyclicIterator:
    def __init__(self, obj: Iterable):
        self.obj = obj
        self.iterator = iter(self.obj)

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            x = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.obj)
            x = next(self.iterator)
        return x
            

def test_1():
    x = [1,2,3]
    iter_obj = CyclicIterator(x)
    assert [next(iter_obj) for _ in range(5)] == [1, 2, 3, 1, 2]

def test_2():
    x = range(5)
    iter_obj = CyclicIterator(x)
    assert [next(iter_obj) for _ in range(10)] == [0, 1, 2, 3, 4] * 2

def test_3():
    x = set([2,1])
    iter_obj = CyclicIterator(x)
    assert [next(iter_obj) for _ in range(5)] == [1, 2, 1, 2, 1]

x = [4, 5, 6]
iter_obj = CyclicIterator(x)
iter_o = iter(iter_obj)
for _ in range(10):
    print(next(iter_o), end=' ')