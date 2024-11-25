import math
from typing import Union, Tuple, TypeAlias


Number: TypeAlias = Union[float, int]

class ComplexNumber:
    def __init__(self, *, x: Number=0, y: Number=0, 
                 phi: Number=0, rho: Number=0, form: str = 'alg'):
        assert form in ['alg', 'polar'], "complex number can be given either in algebraic or polar form only"
        if form == 'polar':
            self.init_from_polar(phi, rho)
        else:
            self.init_from_alg(x, y)
            
    def init_from_alg(self, x: Number, y: Number) -> None:
        ComplexNumber.__is_number(x, 'x')
        ComplexNumber.__is_number(y, 'y')
        phi, rho = self.alg2polar(x, y)
        self._x = x
        self._y = y
        self._phi = phi
        self._rho = rho

    def init_from_polar(self, phi: Number, rho: Number) -> None:
        ComplexNumber.__is_number(phi, 'phi')
        ComplexNumber.__is_number(rho, 'rho')
        if rho < 0:
            raise ValueError('radius rho must be non-negative')
        phi = phi % 2* math.pi
        x, y = self.polar2alg(phi, rho)
        self._x = x
        self._y = y
        self._phi = phi
        self._rho = rho

    def alg2polar(self, x: Number, y: Number) -> Tuple[Number, Number]:
        rho = math.sqrt(x*x+y*y)
        if x == 0:
            if y > 0:
                phi = math.pi / 2
            else:
                phi = -math.pi / 2
        else:
            phi = math.atan(y/x)
        return phi, rho
        
    def polar2alg(self, phi: Number, rho: Number) -> Tuple[Number, Number]:
        x = rho * math.cos(phi)
        y = rho * math.sin(phi)
        return x, y

    @staticmethod
    def __is_number(num: Number, varname: str) -> None:
        if not isinstance(num, Number):
            raise ValueError(f"Input variable {varname} must be either int or float")

    @property
    def x(self) -> Number:
        return self._x

    @x.setter
    def x(self, val: Number) -> None:
        self.init_from_polar(x=val, y=self.y)

    @property
    def y(self) -> Number:
        return self._y

    @y.setter
    def y(self, val: Number) -> None:
        self.init_from_polar(x=self.x, y=val)
    
    @property
    def phi(self) -> Number:
        return self._phi

    @phi.setter
    def phi(self, val: Number) -> None:
        self.init_from_polar(rho=self.rho, phi=val, form='polar')

    @property
    def rho(self) -> Number:
        return self._rho

    @rho.setter
    def rho(self, val: Number) -> Number:
        self.init_from_polar(rho=val, phi=self.phi, form='polar')

    def get_alg_form(self) -> Tuple[Number, Number]:
        return self.x, self.y

    def get_polar_form(self) -> Tuple[Number, Number]:
        return self.phi, self.rho

    def __add__(self, sec_obj):
        return ComplexNumber(x=(self.x + sec_obj.x), y=(self.y + sec_obj.y))

    def __sub__(self, sec_obj):
        return ComplexNumber(x=(self.x - sec_obj.x), y=(self.y - sec_obj.y))

    def __mul__(self, sec_obj):
        coef = self.rho*sec_obj.rho
        return ComplexNumber(x=coef*math.cos(self.phi+sec_obj.phi), 
        y=coef*math.sin(self.phi+sec_obj.phi))

    def __truediv__(self, sec_obj):
        if sec_obj.rho == 0:
            raise ValueError("cannot divide by zero")
        coef = self.rho/sec_obj.rho
        return ComplexNumber(x=coef*math.cos(self.phi-sec_obj.phi), 
        y=coef*math.sin(self.phi-sec_obj.phi))
    

if __name__ == '__main__':
    num1 = ComplexNumber(x=3, y=4)
    num2 = ComplexNumber(x=4, y=5)
    num_s = num1+num2
    assert num_s.x == 7
    assert num_s.y == 9
    assert num1.rho == 5
    num_prod = num1*num2
    num_div = num1 / num2

