from typing import Union, List, TypeAlias
import math

Number: TypeAlias = Union[float, int]


class Vector:
    def __init__(self, vals: List[Number]):
        assert isinstance(vals, list), 'input must be a list!'
        n = len(vals)
        incorrect_inds = list(filter(lambda i: not isinstance(vals[i], Number), range(n)))
        report = "".join(map(lambda i: f"ind: {i} val: {vals[i]} type: {type(vals[i])} \n", incorrect_inds))
        assert len(incorrect_inds) == 0, "incorrect values, they must be real numbers: \n{}".format(report)
        self._vec = vals

    def check_vecs(self, other) -> None:
         if not isinstance(other, Vector):
             raise ValueError("both objects must be vectors")
         l1 = len(self)
         l2 = len(other)
         if len(self) != len(other): 
             raise ValueError('dimension mismatch {}!={}'.format(l1, l2))
    
    def __len__(self) -> int:
        return len(self._vec)
    
    def get_euclid_norm(self) -> float:
        return math.sqrt(sum(map(lambda x: x*x, self._vec)))
    
    def get_cos_angle(self, other) -> float:
        self.check_vecs(other)
        eucl1 = self.get_euclid_norm()
        eucl2 = self.get_euclid_norm()
        if eucl1 == 0 or eucl2 == 0:
            ValueError('both norms must be positive, cannot calculate angle with a zero vector')
        return self.get_scalar_prod(other)/(eucl1*eucl2)
    
    def get_scalar_prod(self, other):
        self.check_vecs(other)
        n = len(self._vec)
        return sum(map(lambda i: self._vec[i]*other._vec[i], range(n)))
    
    def __add__(self, other):
        self.check_vecs(other)
        n = len(self._vec)
        new_list = list(map(lambda i: self._vec[i]+other._vec[i], range(n)))
        return Vector(new_list)
    
    def __sub__(self, other):
        self.check_vecs(other)
        n = len(self._vec)
        new_list = list(map(lambda i: self._vec[i]-other._vec[i], range(n)))
        return Vector(new_list)
    
    def __eq__(self, other):
        self.check_vecs(other)
        n = len(self._vec)
        return all(map(lambda i: self._vec[i]==other._vec[i], range(n)))

        
if __name__ == "__main__":
    obj1 = Vector([1,2,3])
    obj2 = Vector([4, 5, 6])
    obj3 = Vector([5, 7, 9])
    obj_s = obj1 + obj2
    assert obj_s == obj3
    print(obj2.get_cos_angle(obj1))
    print(obj1.get_euclid_norm())
    obj_subs = obj2 - obj1
    assert obj_subs == Vector([3, 3, 3])
