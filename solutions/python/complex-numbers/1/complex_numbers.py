import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        return False

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imaginary)
        raise TypeError('Not supported type')

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real,
            )
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real * other, self.imaginary * other)
        raise TypeError('Not supported type')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        if isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imaginary)
        raise TypeError('Not supported type')

    def __rsub__(self, other):
        return self.__mul__(-1).__add__(other)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            return self.__mul__(other.reciprocal())
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError('Cannot divide by zero')
            return ComplexNumber(self.real / other, self.imaginary / other)
        raise TypeError('Not supported type')

    def __rtruediv__(self, other):
        return self.reciprocal().__mul__(other)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)
    
    def reciprocal(self):
        denominator = self.real ** 2 + self.imaginary ** 2
        if denominator == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return ComplexNumber(self.real / denominator, -self.imaginary / denominator)

    def exp(self):
        return ComplexNumber(
            math.e ** self.real * math.cos(self.imaginary),
            math.e ** self.real * math.sin(self.imaginary),
        )
