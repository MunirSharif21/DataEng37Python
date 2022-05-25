from shape import Shape
from rectangle import Rectangle
from square import Square

if __name__ == "__main__":

    rect = Rectangle()
    print(rect)
    print(f"Area: {rect.get_area()}")
    print(f"Perimeter: {rect.get_perimeter()}")

    sqr = Square()
    print(sqr)
    print(f"Area: {sqr.get_area()}")
    print(f"Perimeter: {sqr.get_perimeter()}")
