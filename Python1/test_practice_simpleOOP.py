from simpleOOP import *

if __name__ == '__main__':

    print("##### 1. Animal and Dog #######")
    d = Dog()
    d.whoAmI()
    d.eat()
    d.bark()
    print()

    print("##### 2. Circle #######")
    c = Circle()
    c.setRadius(5)
    print(c.getRadius())
    print(c.area())
    print()