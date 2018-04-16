class Point():
    x = 0.0
    y = 0.0

    def __init__ (self,x,y):
        self.x = x
        self.y = y
        print("Point Constructor")

    def ToString(self):
        return "{X:" + str(self.x) +",Y:" + str(self.y) + "}"

class Circle(Point):    #inheriting from class above
    radius = 0.0

    def __init__ (self,x,y,radius):
        super().__init__(x,y)
        self.radius = radius
        print("Circle constructor")

    def ToString(self):
        return super().ToString() + ",{RADIUS=" + str(self.radius) + "}"

p = Point(10,20)
print(p.ToString())

c = Circle(100,100,50)
print(c.ToString())
