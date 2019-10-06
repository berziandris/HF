class Sztring :

    def __init__(self, p1=""):
        self.string = p1

    def __str__(self):
        return "Ez egy sztring objektum, melynek tartalma: {}".format(self.string)

    def setString(self, p2):
        self.string = p2
        return "Ez egy sztring objektum, melynek tartalma: {}".format(self.string)

    def toUpper(self):
        return "Ez egy sztring objektum, melynek tartalma: {}".format(self.string.upper())

    def toLower(self):
        return "Ez egy sztring objektum, melynek tartalma: {}".format(self.string.lower())

    def bigCapital(self):
        return "Ez egy sztring objektum, melynek tartalma: {}".format(self.string.capitalize())

p = Sztring('ugVbuHjnk')
print(p)
print(p.setString('meGvaLtozTat'))
print(p.toLower())
print(p.toUpper())
print(p.bigCapital())