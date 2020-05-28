# Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle.

class Circle():
    def __init__(self, r):
        #atrybuty
        self.radius = r

    def area(self):
        return 3.14*self.radius**2

    def parimeter(self):
        return 2*3.14*self.radius


newCircle=Circle(4)
print("Pole koła to: ",newCircle.area(), " zaś jego obwód: ",newCircle.parimeter())

