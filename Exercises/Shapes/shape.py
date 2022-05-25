"""
- A rectangle class
- It should have a width and a height
- Give it the methods: get_area() and get_perimeter()
- Give it appropriate str and repr representations
- A square class
- It should have a length
- It needs get_area() and get_perimeter() and appropriate str and repr representations

For tomorrow's round-robin: create an analogy for the pillars of OOP """


class Shape:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def __repr__(self):
        return f"name={self.name}, width={self.width}, height+{self.height}."

    def __str__(self):
        return f"{self.name} W:{self.width} H:{self.height}"
