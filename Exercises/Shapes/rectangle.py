from shape import Shape


class Rectangle(Shape):
    def __init__(self):
        super().__init__(
            name="Rectangle",
            width=10,
            height=10
        )

