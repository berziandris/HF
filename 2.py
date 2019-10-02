class Vektor :

    def __init__(self, p1=0, p2=0, p3=0, p4=0):
        self.origox = p3
        self.origoy = p4
        self.x = p1
        self.y = p2

    def __str__(self):
        return "A vektor kordinátái: ({},{})".format(self.x, self.y)

    def getHossz(self):
        return ((self.x - self.origox) ** 2 + (self.y - self.origoy) ** 2) **0.5

    def __add__(self, other):
        return "A vektorok Összege: ({},{})".format(self.x + other.x,self.y + other.y)

    def Hozzaad(self, szam):
        return self.getHossz() + szam

    def __sub__(self, other):
        return "A vektorok különbsége: ({},{})".format(self.x - other.x, self.y - other.y)

    def Kivon(self, szam):
        return self.getHossz() - szam

    def __mul__(self, other):
        return "A vektorok szorzata: ({},{})".format(self.x * other.x, self.y * other.y)

    def Szorzas(self, szam):
        return "A vektor szorzata {}-vel: ({},{})".format(szam, self.x * szam, self.y * szam)

    def __lt__(self, other):
        return self.getHossz() < other.getHossz()

    def __le__(self, other):
        return self.getHossz() <= other.getHossz()

    def __eq__(self, other):
        return self.x == other.x, self.y == other.y

    def __ne__(self, other):
        return self.x != other.x, self.y != other.y

v1 = Vektor(5,5)
v2 = Vektor(3,5)
print(v1)
print(v2)
print(v1.getHossz())
print(v2.getHossz())
print(v1+v2)
print(v1.Hozzaad(2))
print(v1-v2)
print(v1.Kivon(2))
print(v2*v1)
print(v1.Szorzas(2))
print(v1>v2)
print(v1<=v2)
print(v1==v2)
print(v1!=v2)

