from shape import Shape


class Square(Shape):
    def __init__(self):
        super().__init__(
            name="Square",
            width=30,
            height=30
        )
# could get away with a single variable "side" instead of width and height
