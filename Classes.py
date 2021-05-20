class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name


square = Polygon(4, "Square")
print(square.sides)


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Heloo my name is " + self.name)


S1 = People("Jayson", 12)
S1.age = 20
print(S1.myfunc())
print(S1.name)
print(S1.age)


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()
