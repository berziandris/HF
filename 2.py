class Vektor :

    def __init__(self, origox=0, origoy=0):
        self.x = origox
        self.y = origoy

    def __str__(self):
        return "A vektor kordinátái: ({},{})".format(self.x, self.y)

print(Vektor())