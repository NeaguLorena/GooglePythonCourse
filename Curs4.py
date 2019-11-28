class Fraction(object):

    def __init__(self,numa,numi):
        self.numarator = numa
        self.numitor = numi

    def __str__(self):
        return "(" + str(self.numarator) + "," + str(self.numitor) + ")"

    def __add__(self, y):
        if self.numitor == y.numitor:
            return Fraction(self.numarator + y.numitor, self.numitor)
        else:
            return Fraction(self.numitor*y.numarator + self.numarator*y.numitor, self.numitor*y.numitor)
    def __float__(self):
        return

a = Fraction(1,2)
b = Fraction(2,3)
print(a)
print(b)
print(a+b)

class intSet(object):

    def __init__(self,lista):
        self.lista = lista

    def insert(self,el):
        self.lista.append(el)

    def str
