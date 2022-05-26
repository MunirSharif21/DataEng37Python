class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        super().__init__(length, length)


s = Square(5)
print(s.get_area())
print(s.get_perimeter())

print(isinstance(s, Square))  # is the "s" object an instance of Square class?
print(isinstance(Square, Rectangle))  # True
