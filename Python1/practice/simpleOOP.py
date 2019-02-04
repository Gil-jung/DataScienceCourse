class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


class Circle():
    def __init__(self):
        self.pi = 3.141592
        self.radius = None

    def area(self):
        return self.pi * self.radius * self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius