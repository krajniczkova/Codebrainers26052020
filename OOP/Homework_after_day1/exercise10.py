# Write a Python class named Rectangle
# constructed by a length and width and a method which will compute the area of a rectangle.

class Rectangle():
    def __init__(self, l, w):
        # atrybuty obiektu:
        self.length = l
        self.width = w

    # definiujemy metody
    def area(self):
        return self.length*self.width

newRectangle=Rectangle(3,5)
print(newRectangle.area())