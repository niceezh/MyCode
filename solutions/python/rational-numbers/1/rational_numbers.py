import math

class Rational:
    def __init__(self, numer, denom):
        if numer == 0 and denom == 0:
            raise ValueError('Cannot have a rational number with 0 numerator and denominator!')
        common = math.gcd(numer, denom)
        if denom < 0:
            numer = -numer
            denom = -denom
        self.numer = numer // common
        self.denom = denom // common

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numer == other.numer and self.denom == other.denom
        return False

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.denom + self.denom * other.numer
            denom = self.denom * other.denom
            return Rational(numer, denom)
        if isinstance(other, int):
            numer = self.numer + self.denom * other
            denom = self.denom
            return Rational(numer, denom)
        raise TypeError('Invalid type!')

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.denom - self.denom * other.numer
            denom = self.denom * other.denom
            return Rational(numer, denom)
        if isinstance(other, int):
            numer = self.numer - self.denom * other
            denom = self.denom
            return Rational(numer, denom)
        raise TypeError('Invalid type!')

    def __rsub__(self, other):
        return self.__mul__(-1).__add__(other)

    def __mul__(self, other):
        if isinstance(other, Rational):
            numer = self.numer * other.numer
            denom = self.denom * other.denom
            return Rational(numer, denom)
        if isinstance(other, int):
            numer = self.numer * other
            denom = self.denom
            return Rational(numer, denom)
        raise TypeError('Invalid type!')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numer == 0:
                raise ValueError('Cannot divide by 0!')
            numer = self.numer * other.denom
            denom = self.denom * other.numer
            return Rational(numer, denom)
        if isinstance(other, int):
            if other == 0:
                raise ValueError('Cannot divide by 0!')
            numer = self.numer
            denom = self.denom * other
            return Rational(numer, denom)
        raise TypeError('Invalid type!')

    def __rtruediv__(self, other):
        return self.reciprocal().__mul__(other)

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)

    def __pow__(self, power):
        if isinstance(power, int):
            if power >= 0:
                numer = self.numer ** power
                denom = self.denom ** power
            else:
                power = abs(power)
                numer = self.denom ** power
                denom = self.numer ** power
            return Rational(numer, denom)
        if isinstance(power, float):
            numer = self.numer ** power
            denom = self.denom ** power
            return numer / denom
        raise TypeError('Invalid type!')

    def __rpow__(self, base):
        return pow(base, self.numer / self.denom)

    def reciprocal(self):
        return Rational(self.denom, self.numer)
