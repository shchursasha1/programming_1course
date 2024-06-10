import re

class Polynomial(dict):
    def __init__(self, arg, coeff_type=float):
        self.coeff_type = coeff_type
        if isinstance(arg, str):
            self._parse_string(arg)
        elif isinstance(arg, dict):
            super().__init__({int(k): coeff_type(v) for k, v in arg.items()})
        elif isinstance(arg, list):
            super().__init__({i: coeff_type(v) for i, v in enumerate(arg)})
        elif isinstance(arg, (int, float, complex)):
            super().__init__({0: coeff_type(arg)})
        else:
            raise ValueError("Unsupported format for polynomial initialization")
        self._reduce()

    def _parse_string(self, s):
        terms = s.split('+')
        for term in terms:
            term = term.strip()
            if 'x' in term:
                coeff, power = term.split('x')
                if coeff == '':
                    coeff = '1'
                if '^' in power:
                    power = power.split('^')[1]
                else:
                    power = '1'
                self[int(power)] = int(coeff)
            else:
                self[0] = int(term)
        self._reduce

    def _reduce(self):
        for k in list(self.keys()):
            if self[k] == 0:
                del self[k]

    def copy(self):
        return Polynomial(dict(self), self.coeff_type)

    def as_type(self, coeff_type):
        return Polynomial({k: coeff_type(v) for k, v in self.items()}, coeff_type)

    def __str__(self):
        return ' + '.join([f'{v}x^{k}' if k != 0 else f'{v}' for k, v in sorted(self.items(), reverse=True)])

    def __repr__(self):
        return f'Polynomial({dict(self)}, coeff_type={self.coeff_type.__name__})'

    def __iter__(self):
        return iter(sorted(self.items()))

    def __add__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Polynomial({0: other}, self.coeff_type)
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        result = self.copy()
        for k, v in other.items():
            if k in result:
                result[k] += v
            else:
                result[k] = v
        result._reduce()
        return result

    def __sub__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Polynomial({0: other}, self.coeff_type)
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        result = self.copy()
        for k, v in other.items():
            if k in result:
                result[k] -= v
            else:
                result[k] = -v
        result._reduce()
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Polynomial({0: other}, self.coeff_type)
        if not isinstance(other, Polynomial):
            return NotImplemented
        
        result = Polynomial({}, self.coeff_type)
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                if k1 + k2 in result:
                    result[k1 + k2] += v1 * v2
                else:
                    result[k1 + k2] = v1 * v2
        result._reduce()
        return result

    def __call__(self, value):
        result = 0
        for k, v in self.items():
            result += v * (value ** k)
        return result

    def __truediv__(self, value):
        if not isinstance(value, (int, float, complex)):
            return NotImplemented
        
        result = Polynomial({}, self.coeff_type)
        for k, v in self.items():
            result[k] = v / value
        result._reduce()
        return result

    def derivative(self):
        result = Polynomial({}, self.coeff_type)
        for k, v in self.items():
            if k > 0:
                result[k - 1] = v * k
        result._reduce()
        return result

    def primitive(self):
        result = Polynomial({}, self.coeff_type)
        for k, v in self.items():
            result[k + 1] = v / (k + 1)
        return result


if __name__ == "__main__":
    p1 = Polynomial("3 + 3x^2 + 4x^3")
    p2 = Polynomial({0: 1, 1: 2, 2: 3})
    p3 = Polynomial([1, 2, 3, 4])
    p4 = Polynomial(5)

    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p3: {p3}")
    print(f"p4: {p4}")

    p_sum = p1 + p2
    p_diff = p1 - p2
    p_prod = p1 * p2
    p_div = p1 / 2
    p_derivative = p1.derivative()
    p_primitive = p1.primitive()

    print(f"p1 + p2: {p_sum}")
    print(f"p1 - p2: {p_diff}")
    print(f"p1 * p2: {p_prod}")
    print(f"p1 / 2: {p_div}")
    print(f"p1 derivative: {p_derivative}")
    print(f"p1 primitive: {p_primitive}")
    print(f"p1 in x=1: {p1.__call__(1)}")
