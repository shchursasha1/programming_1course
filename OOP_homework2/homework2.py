import math

class RationalNumber:

    __slots__ = ['_numerator', '_denominator']

    def __init__(self, numerator, denominator):
        """ Initialize a rational number with a numerator and a denominator.

        :param numerator: the numerator of the rational number
        :param denominator (cannot be zero): the denominator of the rational number
        """
        if denominator == 0:
            raise ZeroDivisionError('denominator cannot be zero')
        self._numerator, self._denominator = self._reduce(int(numerator), int(denominator))

    @property
    def numerator(self) -> int:
        return self._numerator
    
    @property
    def denominator(self) -> int:
        return self._denominator
    
    def is_integer(self) -> bool:
        return self._denominator == 1

    @classmethod
    def from_string(cls, string):
        try:
            numerator, denominator = map(int, string.strip().split('/'))
            return cls(numerator, denominator)
        except ValueError:
            return cls(int(string), 1)  # Якщо числе не раціональне, повертає int(string), а не cls(int(string), 1), бо це в майбутньому викликає помилку
        
    @staticmethod
    def _reduce(numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return numerator // gcd, denominator // gcd
    
    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._numerator * other._denominator + other._numerator * self._denominator, self._denominator * other._denominator)
        return self + type(self)(other, 1)
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._numerator * other._denominator - other._numerator * self._denominator, self._denominator * other._denominator)
        return self - type(self)(other, 1)
    
    def __rsub__(self, other):
        return other - self

    def __mul__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._numerator * other._numerator, self._denominator * other._denominator)
        return self * type(self)(other, 1)
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        try:
            if isinstance(other, type(self)):
                return type(self)(self._numerator * other._denominator, self._denominator * other._numerator)
            return self / type(self)(other, 1)
        except ZeroDivisionError:
            raise ZeroDivisionError('division by zero')

    def __rtruediv__(self, other):
        return other / self
    
    def __pow__(self, power):
        if power < 0:
            return type(self)(self._denominator ** abs(power), self._numerator ** abs(power))
        return type(self)(self._numerator ** power, self._denominator ** power)
    
    def __abs__(self):
        return type(self)(abs(self._numerator), abs(self._denominator))
    
    def sign(self):
        return -1 if self._numerator * self._denominator < 0 else 1

    def inverse(self):
        return type(self)(self._denominator, self._numerator)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self._numerator == other._numerator and self._denominator == other._denominator
        return self == type(self)(other, 1)
    
    def __gt__(self, other): # Перевизначення оператора порівняння '>'
        if isinstance(other, type(self)):
            return self._numerator * other._denominator > other._numerator * self._denominator
        return self > type(self)(other, 1)
    
    def __lt__(self, other): # Перевизначення оператора порівняння '<'
        if isinstance(other, type(self)):
            return self._numerator * other._denominator < other._numerator * self._denominator
        return self < type(self)(other, 1)

    def __repr__(self):
        return f'{type(self)}({self._numerator}, {self._denominator})'
    
    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        return f'{self._numerator}/{self._denominator}'
    

def read_numbers(filename) -> list:
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            numbers.append(RationalNumber.from_string(line))
    return numbers


def read_coeffs(file_path) -> list:
    coeffs = []
    with open(file_path, 'r') as file:
        for line in file:
            coeffs.append([RationalNumber.from_string(string.strip()) for string in line.split(',')])
    return coeffs


def max_number(numbers):  # 84
    return max(numbers)


def max_number_mod(numbers):  # -100
    return max(numbers, key=lambda x: abs(x))


def arithmetic_mean(numbers): # -3072675416586181634630752748701831382211787/-6835330904873772271032726366207088584000000
    return sum(numbers) / len(numbers)


def evaluate_polynomial(coeffs, x):
    return sum(coeff * x**i for i, coeff in enumerate(reversed(coeffs)))

def solve_quadratic(a, b, c):
    try:
        disc = b*b - 4*a*c
        if disc.numerator < 0:
            return []
        elif disc.numerator == 0:
            return [-1*b / (2*a)]
        else:
            sqrt_disc = math.sqrt(disc.numerator / disc.denominator)
            return [(-1*b - sqrt_disc) / (2*a), (-1*b + sqrt_disc) / (2*a)]
    except ValueError: # If any of this exceptions occurs, return an empty list (there's no roots)
        return []
    except ZeroDivisionError:
        return []

def solve_linear(b, c):
    try:
        return [-1*c / b]
    except ZeroDivisionError:
        return []

def find_rational_roots(coeffs):
    p = [i for i in range(1, abs(coeffs[-1].numerator) + 1) if coeffs[-1].numerator % i == 0]
    q = [i for i in range(1, abs(coeffs[0].numerator) + 1) if coeffs[0].numerator % i == 0]
    roots = []
    for i in p:
        for j in q:
            if evaluate_polynomial(coeffs, i/j) == 0:
                roots.append(i/j)
            if evaluate_polynomial(coeffs, -i/j) == 0:
                roots.append(-i/j)
    return roots

def solve_polynomial(coeffs):
    degree = len(coeffs) - 1
    if degree == 1:
        return solve_linear(*coeffs)
    elif degree == 2:
        a, b, c = coeffs
        if a == 0:
            return solve_linear(b, c)
        else:
            return solve_quadratic(*coeffs)
    elif all(coeff.is_integer() for coeff in coeffs):
        return find_rational_roots(coeffs)
    else:
        return []


def main():
    coefficients = read_coeffs('input2.txt')
    results = []

    for coeff in coefficients:
        value_at_1 = evaluate_polynomial(coeff, 1)
        roots = solve_polynomial(coeff)
        results.append((value_at_1, roots))

    with open("output.txt", 'w') as file:
        for i, (value, roots) in enumerate(results):
            file.write(f"Polynomial {i + 1}:\n")
            file.write(f"Value at x = 1: {value}\n")
            if roots:
                file.write(f"Roots: {', '.join(str(root) for root in roots)}\n")
            else:
                file.write("No rational roots found.\n")

if __name__ == '__main__':
    main()
    print(max_number(read_numbers('input1.txt')))
