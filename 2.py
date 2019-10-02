class Vektor :

    def __init__(self, origox=0, origoy=0):
        self.origox = 0
        self.origoy = 0
        self.x = origox
        self.y = origoy

    def __str__(self):
        return "A vektor kordinátái: ({},{})".format(self.x, self.y)

    def getHossz(self):
        return ((self.x - self.origox) ** 2 + (self.y - self.origoy) ** 2) **0.5

print(Vektor(2,4))
print(getHossz())
