class Komplex:
    def __init__(self, p1, p2):
        self.valos = p1
        self.kepzetes = p2

    def conjugate(self):
        return self.__class__(self.valos, -self.kepzetes)

    def argz(self):
        return math.atan(self.kepzetes / self.valos)

    def __str__(self):
        if self.kepzetes < 0 :
            return "A komplex szám: ({}{}i)".format(self.valos, self.kepzetes)
        return "A komplex szám: ({}+{}i)".format(self.valos, self.kepzetes)

    def __add__(self, other):
        if hasattr(other, 'valos') :
            return self.__class__(self.valos + other.valos, self.kepzetes + other.kepzetes)
        if isinstance(other, int) or isinstance(other, float) :
            return self.__class__(self.valos + other, self.kepzetes)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if hasattr(other, 'valos') :
            return self.__class__(self.valos - other.valos, self.kepzetes - other.kepzetes)
        if isinstance(other, int) or isinstance(other, float) :
            return self.__class__(self.valos - other, self.kepzetes)

    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(other - self.valos, -self.kepzetes)

    def __mul__(self, other):
        if hasattr(other, 'valos') :
            return self.__class__((self.valos * other.valos) - (self.kepzetes * other.kepzetes), self.valos * other.kepzetes + self.kepzetes * other.valos)
        if isinstance(other, int) or isinstance(other, float) :
            return self.__class__(self.valos * other, self.kepzetes * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def konjugalt(self):
        return self.__class__(self.valos, -self.kepzetes)

    def __eq__(self, other):
        return (self.valos == other.valos) and (self.kepzetes == other.kepzetes)

    def __ne__(self, other):
        return (self.valos != other.valos) or (self.kepzetes != other.kepzetes)

k = Komplex(1,-3)
k1 = Komplex(2,5)
k2 = Komplex(2,5)
k3 = Komplex(1,-3)
print(k)
print(k2+k)
print(k-k2)
print(3-k)
print(k*k2)
print(3*k)
print(k.konjugalt())
print(k==k3)
print(k!=k2)
