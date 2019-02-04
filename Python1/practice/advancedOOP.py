class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Pythagoras():
    def __init__(self, x1, y1, x2, y2):
        self.point_one = self.setPointOne(x1, y1)
        self.point_two = self.setPointTwo(x2, y2)

    def setPointOne(self, x, y):
        p1 = Point(x, y)
        return p1.x, p1.y

    def setPointTwo(self, x, y):
        p2 = Point(x, y)
        return p2.x, p2.y

    def getSlope(self):
        return (self.point_two[1] - self.point_one[1]) / (self.point_two[0] - self.point_one[0])

    def getDistance(self):
        return ((self.point_two[0] - self.point_one[0])**2 + (self.point_two[1] - self.point_one[1])**2)**0.5